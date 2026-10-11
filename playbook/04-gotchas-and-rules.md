# Gotchas and hard-won rules

1. **Too many tools fills the context window.** Every connected MCP server puts its tool schemas into the prompt. 10+ servers can use tens of thousands of tokens before you type anything, and tool-selection accuracy drops. Mitigations:
   - Connect per project, not globally.
   - Use toolset filters (GitHub toolsets, Supabase `features=`, PostHog `features=`/`tools=`, Neon `category=`, Chrome DevTools `--slim`).
   - Prefer **skills** (loaded on demand) and **CLIs** (`gh`, `vercel`, `supabase`, `stripe`) when the agent can run a shell.
   - "Code-mode" servers (Cloudflare, Paddle, Appwrite's `search_tools`/`call_tool`) expose 2–4 meta-tools instead of hundreds. That's the direction the industry is moving.
2. **Community MCPs are code running with your credentials.** Tool-poisoning and prompt-injection attacks are real. Prefer vendor-official hosted servers with OAuth. Run `snyk/agent-scan` on your config. Run community servers in ToolHive or Docker MCP Gateway. Pin versions instead of `@latest` for anything with write access.
3. **Prompt injection through "eyes" and "research" tools.** Pages scraped by Firecrawl, Playwright or browser-use can contain instructions. Never pair an unrestricted browsing/scraping MCP with write-capable payments/DB/deploy MCPs in the same autonomous session without human confirmation.
4. **Scope the "hands" servers.** Supabase `read_only=true&project_ref=…`. Stripe restricted keys and test mode. Polar/Paddle sandbox endpoints. Convex keeps production disabled by default; leave it that way. Never point an agent at prod DB credentials.
5. **Archived or moved repos are everywhere in tutorials.** Browserbase, PostHog, Sanity, Railway, Semgrep, Prisma, ElevenLabs, Penpot, Ahrefs, Automattic WordPress MCP, Storybook MCP, Nhost and appcypher's awesome list are all archived. Sentry's repo now redirects to `getsentry/toolkit`; Stripe's `agent-toolkit` is now `stripe/ai`. Check the vendor docs page, not a 2025 blog post.
6. **Telemetry defaults.** Chrome DevTools MCP (`--no-usage-statistics`), Shopify Dev MCP and others send usage data by default.
7. **Figma remote vs desktop conflict.** If both are configured, clients may resolve to the desktop server and miss the remote-only write tools. Give them distinct names.
8. **Free tiers are not production plans.** Vercel Hobby is non-commercial. Supabase free projects pause when idle. Render free services spin down. Recheck vendor pricing before launch; these notes weren't re-checked line by line against each pricing page.
9. **Skills are also code.** SKILL.md packs can bundle scripts. Review popular community packs (Superpowers, ui-ux-pro-max, taste-skill, impeccable) before giving them shell access. Star counts in the 100k range don't prove a pack is safe.
