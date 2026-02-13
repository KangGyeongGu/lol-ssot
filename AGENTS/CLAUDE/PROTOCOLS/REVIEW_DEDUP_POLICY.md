# Review Deduplication Policy

Policy
- SSOT mismatch has priority when SSOT and QUALITY findings overlap on the same root cause.
- QUALITY findings that are independent remain separate tasks.
- No finding should be silently dropped.

Required Actions
1. Identify overlap candidates by domain + code evidence + behavioral symptom.
2. Choose primary finding:
   - SSOT if root cause is spec non-compliance.
   - QUALITY if no spec mismatch exists.
3. Record traceability:
   - Keep merged IDs in SOURCE_FINDINGS.
   - Keep merged report filenames in RELATED_REPORTS.

Output Requirement
- MASTER_PLAN.md must include a "Deduplication decisions" section listing merged and independent findings.
