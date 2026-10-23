# LinkedIn organic growth for a solo founder: the one-buyer, proof-first system

An 8-step system for getting leads from LinkedIn posts with no ads, no team and no ghostwriter. Adapted from a solo founder's X article. **The author's results are their own and unverified:** about 9.4M impressions in 12 months, 708k in one week, one post with 526k impressions and 4,202 comments, 2,016 leads in 30 days, ~€30K revenue, €0 on ads. Their product names, tool promotion, course and prices are omitted (this repo is free-only); where they used a paid automation tool I give the generic version and the risks.

- **Core claim:** ads rent attention; organic compounds it. Old posts keep bringing followers, leads and DMs.
- **Three rules:** every post is written for **one buyer**; every post **asks for something**; no comment waits more than a few minutes for a reply.
- **Related:** [audience without a personal brand](audience-without-personal-brand.md), [weekly trend picks](claude-head-of-content-trends.md), [Humanizer skill](../playbook/06-claude-repos-that-earn-their-place.md) (cleans AI-sounding copy).

## Setup: `context.md` (do this first)

Every prompt below starts with **"Read context.md first."** This one page stops the model sounding like everyone else. Write it once:

```markdown
# context.md
## Who I am and what I sell
[offer, price, who it's for]
## My buyer
[job, age, what they earn, what they've tried, what they fear, the exact words they use for their problem]
## My real numbers and proof
[results, screenshots, dates, failures: only true ones]
## Words and styles I never want in my posts
[banned phrases, hype words, clichés]
```

## 1. Post for one buyer, every week, with proof

Organic fails when you post for "everyone". It works when one person reads a post and thinks *"he did the thing I want"*. Every post carries **proof**: a number, a screenshot, a date, or a failure. Not advice from a mountain top.

> Read context.md first. Describe my buyer in 10 lines: job, age, what they earn, what they've tried, what they fear, the exact words they use to describe their problem. Then give me 15 post ideas where I show proof of something this buyer wants. Each idea must use a real number or screenshot from context.md. If a number is missing, write [TO FILL] and ask me.

The output is the **menu you pick from on Monday**, not the post.

## 2. Steal your own winners

Your account already knows what works. Weekly: sort your posts by impressions, look at the top 3, write the next post in the same shape on a new topic. Growth comes from a few big spikes, so find what caused them and repeat it.

> Read context.md first. Here are my last 30 posts with impressions, comments and leads. Group them by format (hook type, length, image or not, call to action). Tell me which 2 formats drove most of the **leads, not the likes**. Then write 3 new posts in those formats, on topics I haven't covered yet.

**Judge by leads, not likes:** 40K impressions with 600 leads beats 200K with 12.

## 3. Make every post ask for a comment

A post that asks for nothing is read and forgotten. The best posts give away something useful (a template, prompt pack, checklist) and ask for a **one-word comment** to get it. That tells LinkedIn the post is starting a conversation, and tells you who wants what you sell.

> Read context.md first. I want to give away [RESOURCE]. Write 5 hooks for a LinkedIn post that offers it free in exchange for a one-word comment. The word must be short, easy to type on a phone and related to the resource. The post must prove I use this resource myself.

## 4. Answer every comment fast

When a post gets hundreds of comments in an hour, the author's claim is that the algorithm watches what happens next: replies keep the conversation (and the post) alive; silence kills it. The author says this, not a better hook, was the biggest reason reach exploded: **a post that never goes quiet**.

- **Do it by hand** in the first hour after posting. Block the time; reply to everyone, with the resource link.
- **Shortcut without risk:** draft replies in batches with the model (text snippets you paste), and send them yourself.
- **Automating replies and DMs** (the author used a paid LinkedIn automation tool): see [Risks](#risks-and-limits). Check LinkedIn's rules and your own account risk before using any tool that posts, replies or messages for you.

## 5. Turn comments into DMs, DMs into emails

A comment is not a lead. An email is.

```text
Comment the keyword -> get the resource by DM within minutes -> the resource sits on a page that asks for an email
-> they join your newsletter -> weeks later, some buy
```

No cold message: they asked first.

> Read context.md first. Write the DM people receive after commenting [KEYWORD] on my post. Max 3 lines, friendly, no sales pitch. It thanks them, gives the link to the resource and asks one question about their situation so they reply. Write 3 versions with different tones.

The closing **question** matters: replies create a real conversation and tell you what people need.

## 6. Outbound (optional, light)

Some buyers never see your posts. The author ran an agent for invitations and follow-ups, reviewing everything important before it went out (one campaign: 60 invitations, 19 accepted, 38 conversations, 11 follow-ups, 2 converted). The rule it followed, which is worth using even by hand:

> Only target people who match my buyer profile. Never pitch in the first message. Open with something specific from their profile or their last post. If they don't reply after 2 follow-ups, stop. Flag anyone who mentions a budget or a deadline so I can take over.

## 7. Sell live, at a price that filters

Everything feeds one offer. The author ran a **free live session** for people who came through the funnel and sold the first seats while still talking; then raised the price. Principles (their specific product and prices omitted):

- A page must convince a stranger alone at midnight. **A live session lets people ask the one question that stops them** and hear the answer.
- **A higher price filters.** At a low price you explain the product daily to people who never open it; at a higher price people arrive already decided.
- Early-buyer pricing with a clear cut-off creates a reason to decide.
- The best proof is unprompted DMs from people you never cold messaged.

## 8. Run the weekly routine

| Day | Do |
|---|---|
| Mon | Pick from the idea menu; write 2-3 posts with proof (draft with the model, edit in your voice) |
| Post days | Post, then answer comments for the first hour; send the resource to commenters |
| Fri | Open analytics: top 3 posts by **leads**; log their format; plan next week's copies |
| Monthly | Review the funnel: comments → DMs → emails → buyers; fix the weakest step |

An agent connected to your analytics can do the reading for you: *"Look at my posts from the last 7 days. Which brought the most leads and why do you think it worked?"*

---

## Risks and limits

| Point | Caution |
|---|---|
| **Results** | The author's numbers (impressions, leads, revenue, "Top 2% in France") are unverified, and one account's experience. Your niche, audience and timing will differ. |
| **Automation** | Tools that reply, DM or send invitations automatically can break LinkedIn's User Agreement and put your account at risk of restriction. Their use is your decision; check the current rules first. The safer path is manual replies plus batch-drafted text. |
| **Email capture** | Collect emails with clear consent and an unsubscribe route (GDPR in the EU; CAN-SPAM in the US). Don't add people to a newsletter without telling them. |
| **Comment-for-resource posts** | These can feel like engagement bait, and LinkedIn can change how it treats them. Make the resource genuinely good. |
| **AI-written posts** | The author mostly wrote with Claude. Edit for your real voice and facts: use real numbers only (the `[TO FILL]` rule), and don't claim results you don't have. |
| **Time** | "Organic isn't free. It costs time." The system lowers the cost, not to zero. |
| **Selling** | Don't promise income outcomes you can't back up. |
