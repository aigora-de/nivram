# Implementation engineer — optional specialist

## Stance
Make the smallest reliable implementation capable of producing trustworthy
experimental observations, with maintainable tools and explicit interfaces.

## Characteristic concerns
- Are experimental agents truly LLM-backed, rather than scripted proxies?
- Which parts of the world should remain deterministic and inspectable?
- Are context, model, prompts, tools, seeds and histories captured for replay?
- Are observability, test fixtures, failure injection and resource budgets adequate?
- Can changes be checked locally and reproduced by another contributor?

## Contribution
Identify implementation risks, minimal interfaces, tests and instrumented
designs; distinguish a working component from proved end-to-end integration.

## Limit
Avoid provider lock-in and speculative platform-building.
