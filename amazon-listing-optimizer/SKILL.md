---
name: amazon-listing-optimizer
description: Create, audit, rewrite, localize, and experiment with Amazon product listings using verified product facts, customer-search evidence, conversion principles, and marketplace-aware compliance checks. Use for titles, bullets, descriptions, backend search terms, image briefs, A+ Content, and listing QA; do not invent claims or publish changes without explicit authorization.
---

# Amazon Listing Optimizer

Produce a truthful, shopper-readable listing that improves discoverability and purchase confidence. Treat optimization as a measurable hypothesis, not a guaranteed ranking or sales outcome.

## Select the mode

- **Create**: build a listing from a product brief and evidence.
- **Audit**: diagnose an existing listing and prioritize changes.
- **Rewrite**: return improved fields while preserving verified facts.
- **Localize**: adapt intent, units, language, claims, and conventions for a named Amazon marketplace; do not merely translate.
- **Experiment**: create materially different A/B variants and a measurement plan.

If the task includes restricted, regulated, medical, ingestible, cosmetic, children’s, pesticide, environmental, safety, or certification claims, read [references/compliance.md](references/compliance.md). For field construction, read [references/field-playbook.md](references/field-playbook.md). For audits or experiments, also read [references/measurement.md](references/measurement.md).

## Establish the evidence base

Before drafting, collect or infer only what the provided evidence supports:

1. Marketplace, language, category/product type, and parent/variation context.
2. Brand, model, quantity, size, color, material, dimensions, compatibility, package contents, and operating limits.
3. Target shopper, jobs-to-be-done, use cases, objections, differentiators, and likely return reasons.
4. Keyword evidence with source and metrics when available: Search Query Performance, Brand Analytics, Product Opportunity Explorer, ad search-term reports, search suggestions, or third-party tools.
5. Existing listing, reviews/Q&A, competitor observations, image assets, and category style guide.

Build a private **fact ledger** with `fact`, `source`, and `confidence`. Never turn a competitor statement, an image guess, or common category behavior into a product fact. Mark unsupported information as `[NEEDS EVIDENCE]`; ask only for missing facts that materially affect accuracy or compliance.

When browsing is requested or available, favor current Amazon policy and seller data over generic SEO articles. Do not copy competitor wording, brand names, images, review text, or protected claims.

## Optimize in this order

1. **Accuracy and compliance** — remove unsupported, prohibited, contradictory, and variation-inconsistent content.
2. **Offer comprehension** — make product identity, quantity, size, compatibility, and primary benefit immediately clear.
3. **Search relevance** — map high-intent phrases to the most suitable fields without stuffing or false relevance.
4. **Conversion clarity** — translate features into evidenced benefits, handle objections, and set accurate expectations.
5. **Creative completeness** — specify images/A+ modules that prove, demonstrate, compare, size, and explain.
6. **Measurement** — identify one high-impact hypothesis at a time and define success and guardrail metrics.

Do not optimize copy when the larger constraint is offer-level: price, availability, delivery promise, reviews, variation structure, or Featured Offer eligibility. Report that constraint separately.

## Keyword allocation

Cluster terms by shopper intent rather than repeating a raw list.

- Put the primary product phrase and decisive differentiator early in the title when truthful.
- Use bullets for secondary phrases that naturally support a feature, benefit, use case, size, or compatibility fact.
- Use the description/A+ for education, objection handling, scenarios, and semantic coverage.
- Reserve backend search terms for relevant synonyms, alternate names, abbreviations, and residual terms not already covered.
- Exclude competitor trademarks, ASINs, irrelevant traffic terms, subjective superlatives, and unsupported audiences or uses.

When keyword metrics are absent, label prioritization as qualitative. Never fabricate volume, rank, conversion, or competitor performance.

## Drafting rules

- Lead with information, not hype. Prefer concrete nouns, quantities, materials, mechanisms, and compatibility facts.
- Express `feature → shopper consequence → use context` only when each link is defensible.
- Surface exclusions and limits that prevent returns; do not bury material caveats.
- Keep one main idea per bullet and order bullets by purchase impact, not by keyword volume alone.
- Avoid repetition, keyword stuffing, all caps, emojis, price/promotion language, review claims, guarantees, urgency, and contact or external-link content.
- Treat category and marketplace templates as authoritative when they differ from general guidance.
- Do not mutate a live listing, upload assets, or publish content unless the user explicitly requests that operation and confirms the final fields.

## Required deliverable

Return the following sections unless the user asks for a narrower output:

1. **Assumptions and evidence gaps** — material unknowns only.
2. **Risk flags** — compliance, factual, variation, keyword, and expectation risks.
3. **Optimized listing** — title, five bullets when the category supports them, description, and backend search terms.
4. **Keyword map** — phrase, intent, evidence/source, assigned field, and inclusion rationale.
5. **Image and A+ brief** — main image check plus a sequenced secondary-image/module plan; label claims that need proof.
6. **Change rationale** — the few changes most likely to affect comprehension, relevance, or conversion.
7. **Experiment plan** — hypothesis, variant, primary metric, guardrails, minimum run condition, and decision rule.
8. **QA result** — pass/fail/warn with unresolved evidence requests.

Use [references/output-template.md](references/output-template.md) when the user wants a complete package. If the listing is available as JSON, run `python3 scripts/lint_listing.py listing.json` and incorporate its findings. The linter is a conservative preflight, not a substitute for Seller Central’s current category validator.

## Final quality gate

Before delivery, verify:

- Every specification and claim traces to evidence.
- Product identity and primary differentiator are clear without reading every field.
- Important keywords are relevant, readable, and intentionally allocated.
- Title complies with current known general rules and any supplied category rule.
- Bullets are distinct, concise, and free of promotional/refund language.
- Backend terms add coverage instead of duplicating visible copy.
- Images/A+ prove the most important claims and clarify scale, contents, operation, and limitations.
- Proposed copy is original and contains no competitor trademarks.
- The experiment changes a meaningful variable and does not promise a result.

Current research basis and official links are maintained in [references/sources.md](references/sources.md).
