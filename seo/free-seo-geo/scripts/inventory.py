#!/usr/bin/env python3
"""Inventory a website repo for the free-seo-geo skill.

Reports what the project already ships, which free tools are installed,
which are available, and what the user must authorize. Does not read .env
files or print secrets.

Usage:
  python3 inventory.py /absolute/path/to/the/website
"""

from __future__ import annotations

import os
import re
import shutil
import sys
from pathlib import Path

SKIP_DIRS = {
    "node_modules",
    ".git",
    ".next",
    "dist",
    "build",
    "coverage",
    ".venv",
    "venv",
    "vendor",
    "out",
    ".turbo",
    ".cache",
}

# id, job, bucket, detect tokens, repo
# bucket: no-account | needs-user | conditional | paid
TOOLS = [
    ("chrome-devtools-mcp", "Lighthouse SEO and performance on live pages", "no-account",
     ["chrome-devtools-mcp", "chrome-devtools"], "https://github.com/ChromeDevTools/chrome-devtools-mcp"),
    ("lighthouse", "Single-URL Lighthouse run", "no-account",
     ["lighthouse"], "https://github.com/GoogleChrome/lighthouse"),
    ("unlighthouse", "Lighthouse across many URLs", "no-account",
     ["unlighthouse"], "https://github.com/harlan-zw/unlighthouse"),
    ("claude-seo", "Technical, schema, and content audit", "no-account",
     ["claude-seo"], "https://github.com/AgriciDaniel/claude-seo"),
    ("geo-seo-claude", "AI-citation audit (crawlers, llms.txt, schema, quotability)", "no-account",
     ["geo-seo-claude"], "https://github.com/zubair-trabzada/geo-seo-claude"),
    ("geo-optimizer-skill", "Rescore robots, llms.txt, schema, and citability", "no-account",
     ["geo-optimizer-skill", "geo-optimizer"], "https://github.com/Auriti-Labs/geo-optimizer-skill"),
    ("mcp-gsc", "Google Search Console queries, coverage, URL inspection", "needs-user",
     ["mcp-gsc", "google-search-console"], "https://github.com/AminForou/mcp-gsc"),
    ("bing-webmaster", "Bing index and query data", "needs-user",
     ["bing-webmaster", "mcp-server-bing"], "https://github.com/isiahw1/mcp-server-bing-webmaster"),
    ("firecrawl", "Fetch HTML the way a crawler receives it", "needs-user",
     ["firecrawl"], "https://github.com/firecrawl/firecrawl-mcp-server"),
    ("exa", "Check whether AI-search results cite this site", "needs-user",
     ["exa-mcp", "exa"], "https://github.com/exa-labs/exa-mcp-server"),
    ("next-seo", "Meta tags for Next.js Pages Router", "conditional",
     ["next-seo"], "https://github.com/garmeeh/next-seo"),
    ("next-sitemap", "Sitemap for Next.js Pages Router", "conditional",
     ["next-sitemap"], "https://github.com/iamvishnusankar/next-sitemap"),
    ("nuxt-seo", "Technical SEO for Nuxt", "conditional",
     ["nuxt-seo"], "https://github.com/harlan-zw/nuxt-seo"),
    ("astro-seo", "SEO tags for Astro", "conditional",
     ["astro-seo"], "https://github.com/jonasmerlin/astro-seo"),
    ("open-seo", "Paid keyword and backlink data", "paid",
     ["open-seo", "openseo"], "https://github.com/every-app/open-seo"),
    ("dataforseo", "Paid SERP and keyword API", "paid",
     ["dataforseo"], "https://github.com/dataforseo/mcp-server-typescript"),
    ("ahrefs", "Paid backlink API", "paid",
     ["ahrefs"], "https://github.com/ahrefs/ahrefs-mcp-server"),
]

NEEDS_USER_WHY = {
    "mcp-gsc": "Needs the Google account that owns this site's Search Console property. Connect through OAuth. Do not paste credentials into chat. Blocks rank and coverage measurement.",
    "bing-webmaster": "Needs a Bing Webmaster API key for this site. Blocks Bing measurement. Skip unless Bing is in scope.",
    "firecrawl": "Needs a Firecrawl free-tier API key. Blocks crawler-HTML fetch only. Skip when browser tools already show the rendered page.",
    "exa": "Needs an Exa free-tier API key. Blocks the post-fix citation check.",
}


def skill_roots(workspace: Path) -> list[Path]:
    home = Path.home()
    roots = [
        workspace / ".cursor" / "skills",
        workspace / ".agents" / "skills",
        workspace / ".claude" / "skills",
        home / ".agents" / "skills",
        home / ".cursor" / "skills",
        home / ".claude" / "skills",
    ]
    store = home / "Library" / "Application Support" / "Cursor" / "AgentStores"
    if store.is_dir():
        roots.extend(p for p in store.glob("**/files/skills") if p.is_dir())
    return [p for p in roots if p.is_dir()]


def mcp_files(workspace: Path) -> list[Path]:
    home = Path.home()
    candidates = [
        workspace / ".cursor" / "mcp.json",
        workspace / ".mcp.json",
        workspace / "mcp.json",
        home / ".cursor" / "mcp.json",
        home / ".claude.json",
        home / ".claude" / "mcp.json",
    ]
    return [p for p in candidates if p.is_file()]


def token_hit(blob: str, token: str) -> bool:
    return re.search(rf"(?<![a-z0-9]){re.escape(token.lower())}(?![a-z0-9])", blob) is not None


def installed_names(workspace: Path) -> dict[str, list[str]]:
    found: dict[str, list[str]] = {}

    def add(tool_id: str, where: str) -> None:
        rows = found.setdefault(tool_id, [])
        if where not in rows:
            rows.append(where)

    for root in skill_roots(workspace):
        for path in root.rglob("SKILL.md"):
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")[:800]
            except OSError:
                continue
            name_line = next((line for line in text.splitlines() if line.startswith("name:")), "")
            blob = f"{path.parent.name}\n{name_line}".lower()
            for tool_id, _job, _bucket, tokens, _repo in TOOLS:
                if any(token_hit(blob, token) for token in tokens):
                    add(tool_id, str(path.parent))

    for path in mcp_files(workspace):
        try:
            blob = path.read_text(encoding="utf-8", errors="ignore").lower()
        except OSError:
            continue
        for tool_id, _job, _bucket, tokens, _repo in TOOLS:
            if any(token_hit(blob, token) for token in tokens):
                add(tool_id, str(path))

    for tool_id, _job, _bucket, tokens, _repo in TOOLS:
        for token in tokens:
            exe = shutil.which(token)
            if exe:
                add(tool_id, exe)
            local = workspace / "node_modules" / ".bin" / token
            if local.exists():
                add(tool_id, str(local))
    return found


def detect_framework(workspace: Path) -> str:
    has_next = any((workspace / n).exists() for n in ("next.config.ts", "next.config.js", "next.config.mjs"))
    has_app = (workspace / "app").is_dir() or (workspace / "src" / "app").is_dir()
    has_pages = (workspace / "pages").is_dir() or (workspace / "src" / "pages").is_dir()
    if has_next and has_app:
        return "next-app"
    if has_next and has_pages:
        return "next-pages"
    if has_next:
        return "next"
    if any((workspace / n).exists() for n in ("nuxt.config.ts", "nuxt.config.js")):
        return "nuxt"
    if any((workspace / n).exists() for n in ("astro.config.ts", "astro.config.mjs", "astro.config.js")):
        return "astro"
    if (workspace / "package.json").is_file():
        return "node"
    return "unknown"


def walk_files(workspace: Path, limit: int = 8000) -> list[Path]:
    found: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(workspace):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".git")]
        for name in filenames:
            found.append(Path(dirpath) / name)
            if len(found) >= limit:
                return found
    return found


def rel(workspace: Path, path: Path) -> str:
    try:
        return str(path.relative_to(workspace))
    except ValueError:
        return str(path)


def site_signals(workspace: Path, files: list[Path]) -> dict[str, list[str]]:
    signals: dict[str, list[str]] = {
        "robots": [],
        "sitemap": [],
        "llms": [],
        "jsonld": [],
        "metadata": [],
        "urls": [],
        "notes": [],
    }
    for path in files:
        name = path.name.lower()
        r = rel(workspace, path)
        if name in {"robots.ts", "robots.js", "robots.txt"} or name.startswith("robots."):
            signals["robots"].append(r)
        if "sitemap" in name and path.suffix.lower() in {".ts", ".js", ".xml", ".tsx"}:
            signals["sitemap"].append(r)
        if name in {"llms.txt", "llms-full.txt"} or "llms.txt" in r or "llms-full" in r:
            signals["llms"].append(r)
        if name in {"claude.md", "agents.md"}:
            signals["notes"].append(r)
        if path.suffix.lower() not in {".ts", ".tsx", ".js", ".jsx", ".mjs", ".html", ".vue", ".astro"}:
            continue
        try:
            if path.stat().st_size > 250_000:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        lower = text.lower()
        if ("application/ld+json" in lower or "schema.org" in lower) and len(signals["jsonld"]) < 12:
            signals["jsonld"].append(r)
        if (
            "export const metadata" in text
            or "generateMetadata" in text
            or 'name="description"' in lower
        ) and len(signals["metadata"]) < 12:
            signals["metadata"].append(r)
        if path.name in {
            "layout.tsx",
            "layout.ts",
            "layout.js",
            "next.config.ts",
            "next.config.mjs",
            "next.config.js",
            "astro.config.mjs",
        } or "example" in name:
            for key in ("metadataBase", "NEXT_PUBLIC_SITE_URL", "SITE_URL", "siteUrl"):
                if key in text and len(signals["urls"]) < 8:
                    signals["urls"].append(f"{r} ({key})")
    return signals


def applicable(tool_id: str, framework: str, signals: dict[str, list[str]]) -> bool:
    if tool_id == "next-seo":
        return framework == "next-pages" and not signals["metadata"]
    if tool_id == "next-sitemap":
        return framework == "next-pages" and not signals["sitemap"]
    if tool_id == "nuxt-seo":
        return framework == "nuxt"
    if tool_id == "astro-seo":
        return framework == "astro"
    return True


def emit(title: str, rows: list[str]) -> None:
    print(f"\n## {title}")
    if rows:
        print("\n".join(rows))
    else:
        print("- none")


def main() -> int:
    workspace = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    if not workspace.is_dir():
        print(f"Workspace not found: {workspace}", file=sys.stderr)
        return 1

    framework = detect_framework(workspace)
    files = walk_files(workspace)
    signals = site_signals(workspace, files)
    installed = installed_names(workspace)

    installed_rows: list[str] = []
    available_rows: list[str] = []
    needs_rows: list[str] = []
    na_rows: list[str] = []
    paid_rows: list[str] = []

    for tool_id, job, bucket, _tokens, repo in TOOLS:
        places = installed.get(tool_id, [])
        if bucket == "paid":
            if places:
                paid_rows.append(f"- {tool_id}: installed ({places[0]}) — do not use")
            else:
                paid_rows.append(f"- {tool_id}: not installed — leave it that way")
            continue
        if bucket == "conditional" and not applicable(tool_id, framework, signals):
            na_rows.append(f"- {tool_id}: not applicable to {framework}")
            continue
        if places:
            installed_rows.append(f"- {tool_id}: {job}")
            for place in places[:4]:
                installed_rows.append(f"  - {place}")
            continue
        if bucket == "needs-user":
            needs_rows.append(f"- {tool_id}: {job}. {NEEDS_USER_WHY[tool_id]} {repo}")
        else:
            available_rows.append(f"- {tool_id}: {job} — {repo}")

    print("# free-seo-geo inventory")
    print(f"workspace: {workspace}")
    print(f"framework: {framework}")
    if signals["urls"]:
        print("site url candidates:")
        for hit in signals["urls"]:
            print(f"  - {hit}")
    else:
        print("site url candidates: none — ask the user for the canonical origin")
    if signals["notes"]:
        print("project notes:")
        for note in signals["notes"]:
            print(f"  - {note}")
    else:
        print("project notes: none")

    print("\n## Already in this project")
    for key in ("robots", "sitemap", "llms", "jsonld", "metadata"):
        rows = signals[key]
        if rows:
            print(f"- {key}: present ({len(rows)})")
            for row in rows[:8]:
                print(f"  - {row}")
        else:
            print(f"- {key}: missing")

    emit("Free tools installed", installed_rows)
    emit("Free, no account, not installed", available_rows)
    emit("Needs you", needs_rows)
    emit("Not applicable", na_rows)
    emit("Out of scope (paid)", paid_rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
