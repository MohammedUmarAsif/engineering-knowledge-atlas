# Contributing

Thank you for helping improve the Engineering Knowledge Atlas. Contributions should make the learning system more accurate, navigable, current, or useful, not merely larger.

## Good contributions

- correct a factual, conceptual, code, spelling, or navigation error;
- replace a secondary claim with a primary or authoritative source;
- identify a hidden prerequisite or misleading intuition;
- add a failure mode, trade-off, production implication, or research limitation;
- update a dated tool or specification while preserving the durable concept;
- improve accessibility or reduce unnecessary cognitive load.

## Before opening a pull request

1. Read the [teaching and depth standard](00-meta/teaching-and-depth-standard.md).
2. Follow the [source and copyright policy](00-meta/source-and-copyright-policy.md).
3. Do not commit copyrighted PDFs merely because they are publicly downloadable.
4. Do not include credentials, private data, proprietary material, or generated claims without verification.
5. Run:

   ```bash
   python3 scripts/validate_repository.py
   python3 scripts/docs.py build --strict
   ```

6. Explain what changed, why it improves learning, and which sources support material claims.

Small, focused pull requests are easier to review. Substantial new pathways or structural changes should begin with a discussion issue.
