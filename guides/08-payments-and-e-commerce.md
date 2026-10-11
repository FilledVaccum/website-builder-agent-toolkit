# 8. Payments and e-commerce

> Source: report (researched 2026-10-11). Narrative/extended view; the ranked skills/repos/MCP tables per stage live in catalog/stages/.

| Service | MCP | URL | Official? | Notes |
|---|---|---|---|---|
| **Stripe** | Hosted `https://mcp.stripe.com` (OAuth or restricted key) | https://docs.stripe.com/mcp · repo https://github.com/stripe/ai (1.9k; former `agent-toolkit`) | Official | Use restricted keys and test mode. The MCP includes docs search. |
| **Polar** | Hosted `https://mcp.polar.sh/mcp/polar-mcp` (+ `/polar-sandbox`) | https://polar.sh/docs/integrate/mcp · https://github.com/polarsource/polar (10.4k) | Official | Merchant of Record (handles global tax) built for devs and indies. OSS. |
| Paddle | Hosted `https://mcp.paddle.com/mcp` + sandbox + Docs MCP | https://developer.paddle.com/sdks/ai/paddle-mcp · https://github.com/PaddleHQ/paddle-mcp-server | Official | MoR. Code-mode `search`/`execute` tools. |
| Lemon Squeezy | **No official MCP.** Community ones only (e.g. `atharvagupta2003/mcp-lemonsqueezy`) | https://github.com/lmsqueezy/lemonsqueezy.js | Community | Acquired by Stripe; the SDK hasn't been pushed since Nov 2024. Avoid it for new projects. |
| PayPal | MCP / agent toolkit | https://github.com/paypal/agent-toolkit | Official | — |
| Square | MCP | https://github.com/square/square-mcp-server | Official | — |
| Shopify | Dev MCP `npx -y @shopify/dev-mcp@latest` + AI Toolkit plugin | https://www.npmjs.com/package/@shopify/dev-mcp · https://github.com/Shopify/Shopify-AI-Toolkit | Official | Docs, GraphQL schema and Liquid validation. **Sends telemetry by default.** |

**Top pick:** **Stripe MCP** if you handle tax yourself or only sell in a few countries. **Polar MCP** if you're a solo dev selling globally (a merchant of record handles VAT/GST for you; confirm your country is supported).
