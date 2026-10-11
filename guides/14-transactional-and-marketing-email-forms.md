# 14. Transactional and marketing email, forms, file storage (indie "glue")

> Source: report (researched 2026-10-11). Narrative/extended view; the ranked skills/repos/MCP tables per stage live in catalog/stages/.

| Service | MCP / skill | URL | Official? | Notes |
|---|---|---|---|---|
| **Resend** | Hosted `https://mcp.resend.com/mcp` (OAuth); local `npx resend-mcp` · skills | https://resend.com/docs/mcp-server · https://github.com/resend/resend-mcp · https://github.com/resend/resend-skills | Official | Developer email API that pairs with React Email. Has a free tier. |
| Loops | Hosted `https://mcp.loops.so` (OAuth) | https://loops.so/docs/mcp-server | Official | Marketing + transactional email for SaaS. |
| Postmark | MCP (24 tools) | https://github.com/ActiveCampaign/postmark-mcp | Official | Deliverability-focused transactional email. |
| Tally (forms) | Hosted `https://api.tally.so/mcp` | https://developers.tally.so/api-reference/mcp | Official | Free on all plans (beta). Agent creates forms and reads submissions. |
| Netlify Forms | Through the Netlify MCP | (above) | Official | Zero-backend forms. |
| UploadThing | `npx @uploadthing/mcp-server` | https://www.npmjs.com/package/@uploadthing/mcp-server · https://github.com/pingdotgg/uploadthing (5.3k) | Official | File uploads for Next.js. |
| Cloudflare R2 | Through the Cloudflare MCP | (above) | Official | S3-compatible with no egress fees. |
| Supabase Storage | Through the Supabase MCP | (above) | Official | — |

**Top pick:** **Resend** (MCP + skills) for email. **Tally** for forms when there's no backend.
