# Measurement and iteration

Use this reference for audits, redesigns, and A/B experiments.

## Diagnose the funnel before rewriting

- **Low impressions**: relevance, indexing, category, availability, or demand problem.
- **Impressions but low clicks**: title/main image/price/reviews/delivery or search-intent mismatch.
- **Clicks but low cart adds**: weak value communication, unclear fit, missing proof, or offer mismatch.
- **Cart adds but low purchases**: price, delivery, availability, variation, trust, or checkout friction.
- **High returns/negative reviews**: expectation, fit, quality, compatibility, instructions, or product problem; copy cannot fix a defective product.

Prefer Amazon data when available: Search Query Performance, Search Catalog Performance, Top Search Terms, ad search-term reports, Product Opportunity Explorer, Customer Review Insights, returns themes, business reports, and Manage Your Experiments.

## Audit rubric

Score each dimension `0–2` and explain evidence. Do not collapse the result into a fake precision score when data is missing.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Accuracy | unsupported/contradictory | some gaps | fully traceable |
| Compliance | material risk | needs review | no known issue |
| Identity clarity | unclear offer | understandable | immediate and precise |
| Search relevance | irrelevant/stuffed | partial map | intent-led allocation |
| Benefit clarity | hype/features only | mixed | concrete and evidenced |
| Objection handling | absent | partial | key barriers answered |
| Expectation setting | misleading/omitted | partial | limits and fit clear |
| Creative coverage | missing/repetitive | basic | sequenced proof/education |
| Differentiation | copied/generic | weak | specific and defensible |
| Measurement readiness | no baseline | hypothesis only | metric and decision rule |

Compliance or accuracy score `0` blocks a publish-ready recommendation regardless of total.

## Experiment design

Change one dominant concept per experiment. Variants should be meaningfully different while keeping product facts constant.

Examples:

- Main image: clean product scale emphasis vs. included-components emphasis.
- Title: concise identity-first vs. use-case-first within policy.
- Bullets: performance-first vs. ease-of-use-first ordering.
- A+ hero: mechanism explanation vs. outcome scenario.

For each experiment define:

- Hypothesis and shopper segment.
- Exact field and change.
- Primary metric: click-through, conversion, units sold, or sales when supported by the tool.
- Guardrails: returns, negative feedback, ad efficiency, or policy issues.
- Run condition: sufficient eligible traffic and a stable offer; use Amazon’s experiment confidence/output rather than inventing a universal duration.
- Decision: publish winner, keep control, or gather more data.

Do not change price, ads, inventory, and multiple creative fields simultaneously if the goal is to attribute a listing-content effect.

## Review cadence

- Record the baseline and timestamp before changes.
- Review indexing and suppression after edits.
- Monitor early operational issues without declaring a winner prematurely.
- Revisit keyword allocation when seasonality or query data changes.
- Feed recurring review/return themes into product content and, where appropriate, product development.
