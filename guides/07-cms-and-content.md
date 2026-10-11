# 7. CMS and content

> Source: report (researched 2026-10-11). Narrative/extended view; the ranked skills/repos/MCP tables per stage live in catalog/stages/.

| Name | MCP | URL | Official? | Stars | Notes |
|---|---|---|---|---|---|
| **Sanity** | Hosted `https://mcp.sanity.io` (`npx sanity@latest mcp configure`) | https://www.sanity.io/docs/ai/mcp-server | Official | — | The old repo `sanity-io/sanity-mcp-server` is **archived** in favour of the remote server. |
| Payload | `@payloadcms/plugin-mcp` → `/api/mcp` | https://payloadcms.com/docs/plugins/mcp · https://github.com/payloadcms/payload | Official | 45.2k | Lives inside your Next.js app. Self-hosted and free. Respects access control. |
| Strapi | Built-in MCP (v5.47+, GA in v5.49) at `/mcp` | https://docs.strapi.io/cms/features/strapi-mcp-server · https://github.com/strapi/strapi | Official | 73.3k | Admin-token permissions limit which tools appear. |
| Contentful | MCP | https://github.com/contentful/contentful-mcp-server | Official | 61 | Management API. |
| WordPress | MCP Adapter (Abilities API) | https://github.com/WordPress/mcp-adapter | Official | 1.8k | `Automattic/wordpress-mcp` is **archived/deprecated** in favour of this. |
| Webflow | MCP | https://github.com/webflow/mcp-server | Official | 141 | Data API + Designer. |
| Directus | MCP | https://github.com/directus/mcp | Official | 86 | Self-hostable headless CMS. |
| TinaCMS | No MCP verified | https://github.com/tinacms/tinacms | OSS | 13.8k | Git-backed markdown CMS. Agents can edit the markdown directly. |

**Top pick:** For a marketing or content site, use **markdown/MDX in Git with Astro** (no CMS, so no MCP needed). Once non-developers edit content, use **Sanity remote MCP**. If you want it self-hosted inside Next.js, use **Payload**.
