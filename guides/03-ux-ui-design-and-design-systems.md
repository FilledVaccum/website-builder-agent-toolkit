# 3. UX/UI design and design systems

> Source: report (researched 2026-10-11). Narrative/extended view; the ranked skills/repos/MCP tables per stage live in catalog/stages/.

| Name | Type | URL | Official? | Stars | What it does / why use it |
|---|---|---|---|---|---|
| **Figma MCP (remote)** | MCP (hosted, OAuth) | https://developers.figma.com/docs/figma-mcp-server/ · endpoint `https://mcp.figma.com/mcp` · guide repo https://github.com/figma/mcp-server-guide | Official | guide 2.1k | Design-to-code context. The remote server also **writes to the canvas** (`use_figma`, `generate_figma_design`, code-to-canvas). Remote works on all seats; the desktop server needs a Dev/Full seat. |
| Framelink (Figma-Context-MCP) | MCP | https://github.com/GLips/Figma-Context-MCP | Community | 16.0k | Popular Figma-to-layout MCP that only needs a personal token. |
| shadcn/ui MCP | MCP (built into the shadcn CLI) | https://ui.shadcn.com/docs/mcp · repo https://github.com/shadcn-ui/ui | Official | 125k | Browse, search and install components from shadcn and any registry with natural language. |
| shadcn-ui-mcp-server | MCP | https://github.com/Jpisnice/shadcn-ui-mcp-server | Community | 3.0k | shadcn context for React, Svelte, Vue and React Native. |
| 21st.dev Magic MCP | MCP | https://github.com/21st-dev/magic-mcp | Official (21st.dev) | 6.0k | "v0 inside your IDE." Searches 10k+ React/Tailwind components and generates UI. Paid tiers. |
| Magic UI MCP | MCP | https://github.com/magicuidesign/mcp | Official | 206 | Animated Magic UI components. |
| Canva MCP | MCP (hosted) | https://www.canva.dev/docs/mcp/ | Official | n/a | Generate and edit Canva designs: social images, OG images, decks. |
| **frontend-design skill** | Skill | https://github.com/anthropics/skills · plugin https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design | Official (Anthropic) | 180k / 150k | Picks a bold, intentional visual direction before writing code. Counters the generic "AI slop" look. |
| UI UX Pro Max | Skill | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | Community | 135k | Design-system generator (styles, palettes, font pairings, UX rules) for many stacks. |
| Taste Skill | Skill | https://github.com/Leonxlnx/taste-skill | Community | 94.6k | Stronger visual personality, less generic output. |
| Impeccable | Skill pack | https://github.com/pbakaus/impeccable | Community | 79.7k | Design vocabulary plus critique, audit and polish commands for existing UIs. |
| Vercel `web-design-guidelines` | Skill | https://github.com/vercel-labs/agent-skills | Official (Vercel) | 32.2k | Reviews UI against Vercel's accessibility and UX guidelines. |
| Penpot | OSS design tool | https://github.com/penpot/penpot | Official | 60.9k | Free Figma alternative. Its standalone `penpot-mcp` repo is **archived**. |
| Onlook | Repo | https://github.com/onlook-dev/onlook | Community (OSS) | 26.9k | Visual editor that edits your React code directly. |

**Top pick:** **Figma remote MCP** if a design exists. If not, use the **frontend-design skill** plus **shadcn/ui MCP** (cheapest path to a site that doesn't look generic).
