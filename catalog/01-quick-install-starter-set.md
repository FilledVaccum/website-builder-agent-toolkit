# Quick-install starter set (best free skill + repo + MCP per stage)

| Stage | Skill | Repo | MCP |
|---|---|---|---|
| 1. Planning | Superpowers | Spec Kit | Taskmaster MCP |
| 2. Research | last30days | Firecrawl (or Crawl4AI) | Playwright MCP / Firecrawl MCP |
| 3. Design | UI UX Pro Max + frontend-design | shadcn/ui | Figma remote MCP (or shadcn MCP) |
| 4. Assets | canvas-design (Anthropic) | sharp + Lucide | Hugging Face MCP |
| 5. Frontend | Vercel agent-skills | Next.js / Astro | Context7 |
| 6. Backend | Supabase agent-skills | Supabase | Supabase MCP |
| 7. Auth | Better Auth skills | Better Auth | Better Auth docs MCP |
| 8. CMS | WordPress/Sanity toolkit (if used) | Payload (or MDX in Git) | Sanity MCP / Payload MCP plugin |
| 9. Payments | Stripe skills (stripe/ai) | stripe-node / Polar | Stripe MCP (test mode) |
| 10. Email & forms | Resend skills | React Email + React Hook Form | Resend MCP + Tally MCP |
| 11. Testing | webapp-testing | Playwright | Playwright MCP |
| 12. Performance | addyosmani performance-optimization | Lighthouse / Unlighthouse | Chrome DevTools MCP |
| 13. SEO | marketingskills + claude-seo | next-seo + next-sitemap + schema-dts | mcp-gsc + GA MCP |
| 14. GEO | marketingskills ai-seo | llms.txt spec + framework llms plugin | Chrome DevTools MCP (agentic-browsing audit) |
| 15. Analytics | Sentry skills | PostHog / Umami | Sentry MCP + PostHog MCP |
| 16. VCS & CI | Claude Code commit/review plugins | Claude Code Action | GitHub MCP |
| 17. Hosting | Cloudflare skills | Coolify (self-host) / Vercel CLI | Cloudflare MCP |
| 18. Security | Cloudflare security-audit-skill | Gitleaks + Semgrep | Semgrep MCP |
| 19. Maintenance | Superpowers systematic-debugging | Renovate | Sentry MCP + GitHub MCP |

**Minimal install (about 10 commands):**
```bash
npx skills add obra/superpowers
npx skills add vercel-labs/agent-skills
npx skills add nextlevelbuilder/ui-ux-pro-max-skill
npx skills add coreyhaines31/marketingskills
npx skills add supabase/agent-skills
# MCPs (Claude Code syntax; other clients take the same URL/command)
claude mcp add --transport http context7 https://mcp.context7.com/mcp
claude mcp add playwright -- npx @playwright/mcp@latest
claude mcp add chrome-devtools -- npx -y chrome-devtools-mcp@latest --slim
claude mcp add --transport http supabase "https://mcp.supabase.com/mcp?read_only=true"
claude mcp add --transport http cloudflare https://mcp.cloudflare.com/mcp
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp
claude mcp add --transport http stripe https://mcp.stripe.com
```
(The Context7 URL and the Playwright package name come from the vendors' READMEs; check each README for the current install line.)
