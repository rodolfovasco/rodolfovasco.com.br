---
title: AI traffic in GA4: how to measure ChatGPT and Gemini
description: Visits from ChatGPT, Gemini and Perplexity show up in GA4 as referral or Direct. Learn how to separate that traffic and what it cannot show you.
slug: ai-traffic-in-ga4-how-to-measure
date: 2026-11-23
updated: 2026-11-23
category: analytics
summary: To measure AI assistant traffic in GA4, create a custom channel group that collects the sources of those assistants. Some visits arrive with no referrer and land in Direct, so the number you see is a floor, not the total.
---

**AI traffic in GA4 is the set of sessions that reach your site after someone clicks a link inside an assistant such as ChatGPT, Gemini, Perplexity or Claude.** Measuring it takes a grouping of your own, because GA4 does not always separate these visits from other referrals, and part of them arrive with no identifiable source.

If you are investing in content to be cited by AI, the next question is obvious: is it sending visits? This guide shows how to set up the basic measurement and, just as important, where it stops.

## Why does AI traffic get lost in GA4?

GA4 sorts each session into channels (Organic Search, Referral, Direct and others) based on source and medium. Visits from AI assistants usually arrive as referral, with the assistant's domain as the source, but two things get in the way:

- **They blend with other referrals.** Without a rule of your own, AI visits get diluted among every site that links to you.
- **Visits with no referrer.** According to Terminus, assistant apps on mobile and desktop usually send no referrer, and those sessions fall into Direct. Trackingplan says the same: a visit without a referrer is counted as Direct and stays there.

The sources also disagree on one point. Terminus and Trackingplan describe a default AI assistant channel in GA4, while Seresa stated in October 2026 that Google had not announced a native grouping. Check what your own property shows before you create any rule.

## Which domains go into the rule?

The list below comes from Terminus (updated September 2026). Treat it as a starting point and review it from time to time, because products and domains change.

| Assistant | Source |
|---|---|
| ChatGPT | chatgpt.com (and the older chat.openai.com) |
| Gemini | gemini.google.com (and the older bard.google.com) |
| Perplexity | perplexity.ai and www.perplexity.ai |
| Claude | claude.ai |
| Copilot | copilot.microsoft.com |
| DeepSeek | chat.deepseek.com |
| Grok | grok.com |
| Others | meta.ai, you.com, poe.com |

The same source advises against including generic domains such as openai.com, anthropic.com or google.com, because they mix in traffic that does not come from assistants. This matters most for google.com, where the sources I read do not allow a reliable split between AI features and regular search.

## How do you create an AI channel in GA4?

The method the sources describe is a custom channel group with a rule on the session source using a regular expression. Step by step:

1. **Open the channel group settings** of your GA4 property and create a custom group. Check Google's documentation for the exact path in your interface, since menus change.
2. **Create a channel called, for example, "AI assistants"** with a condition on source that matches a regular expression.
3. **Paste the expression with the domains.** Terminus publishes this one, anchored to match the whole source: `^(claude\.ai|perplexity\.ai|www\.perplexity\.ai|meta\.ai|you\.com|poe\.com|chatgpt\.com|chat\.openai\.com|gemini\.google\.com|bard\.google\.com|copilot\.microsoft\.com|chat\.deepseek\.com|grok\.com)$`
4. **Place the channel above Referral** in the rule order. Seresa recommends giving it priority over the default group; otherwise the generic channel may classify the session first.
5. **Compare with the source/medium exploration.** If an AI source shows up that is not on your list, add it.

A note on UTMs: according to Terminus, ChatGPT also appends `utm_source=chatgpt.com` to citation links, so part of that traffic arrives tagged as well as referred. Only one of the sources I read says this, and I could not confirm it in OpenAI's documentation during this research. Do not build reports that depend on it without testing.

## What do you do with traffic that lands in Direct?

Do not assume Direct is AI. Branddi, citing Google Analytics support, reminds readers that "(direct) / (none)" means there is no clear source, and that the group should not be handed to AI by guesswork.

What you can do safely:

- **Look at indirect signals.** Trackingplan suggests watching for increases in Direct on deep inner pages, which people rarely type by hand.
- **Ask at the source.** A "how did you find us?" field on forms captures what analytics cannot see.
- **Report the floor.** Present the AI channel number as the minimum observed and say so in the report.
- **Consider server-side measurement.** Seresa argues that server-side tracking recovers part of these visits. The company sells that kind of solution, so treat the claim as a hypothesis to test, not a guarantee.

## Common mistakes

- **Comparing the AI channel with Organic Search as if they were equivalent.** The first is a floor; the second has far more coverage.
- **Using an unanchored regex and catching domains that are not assistants.** Test the expression first.
- **Comparing periods without checking the rule's reach.** Confirm in Google's documentation whether the grouping applies to historical data before comparing.
- **Drawing business conclusions from visits alone.** Look at conversions and session quality, not just volume.

## How do you know it is working?

After some time collecting data, you should see sessions in the new channel with sources that match your list. Cross-check with conversion events: what matters is whether these visits produce contacts, leads or sales. Low volume is normal. Use the data to decide which pages to strengthen, not as a GEO scoreboard.

## Quick questions

:::faq
Q: Does GA4 show ChatGPT traffic automatically?
A: It generally appears as referral, mixed with other sites, and part of it arrives as Direct. A custom channel group separates what has an identifiable source.

Q: Does AI traffic convert better than organic?
A: I am not claiming that. The figures in circulation come from third-party studies I did not verify. Measure conversion on your own site.

Q: Can I measure Google AI Mode and AI Overviews in GA4?
A: The sources I read do not allow a reliable split from regular Google traffic. For that, see Google's Search Console documentation.

Q: Do I need a paid tool?
A: Not for the basics. GA4's custom channel group handles what has an identifiable source. Tools help at scale, but several of the sources I read sell them.

Q: How often should I review the domain list?
A: Every quarter, or whenever an unknown source shows up in your reports.
:::

## Sources

- [Terminus: The "AI Traffic" Channel in GA4: How to Define It Yourself in 2026](https://www.terminusapp.com/blog/ai-traffic-channel-in-ga4/) (the company sells a UTM and taxonomy platform)
- [Trackingplan: How to track ChatGPT and AI traffic in GA4](https://www.trackingplan.com/guides/track-chatgpt-ai-traffic-ga4) (the company sells analytics monitoring)
- [Branddi: How to Measure Traffic from ChatGPT, Gemini, and Perplexity in GA4](https://branddi.com/en/blog/como-medir-trafego-chatgpt-gemini-perplexity-ga4)
- [Seresa: AI Traffic Attribution: Why GA4 Misses Your Best Channel](https://seresa.io/blog/server-side-tracking/ai-traffic-attribution-why-ga4-misses-your-best-channel) (the company sells server-side tracking)

These sources come from tool vendors. Before applying the steps, confirm them in Google's official GA4 channel group documentation.

Want to structure your marketing measurement? Also read [SEO, AEO and GEO: the difference and where to start](/en/articles/seo-aeo-geo-difference-where-to-start/) or [get in touch](#contato).
