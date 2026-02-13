# Review Finding Schema

Purpose
- Standardize raw finding format across SSOT and QUALITY subreview agents.

Required Top-Level Fields
- REVIEW_TYPE: `SSOT` or `QUALITY`
- DOMAIN: review domain key
- SUMMARY: one-paragraph summary
- FINDINGS: list of finding objects

Required Finding Fields
- ID: stable finding id (e.g., `AUTH_USER-S-001`, `API-Q-002`)
- SEVERITY: `Critical | High | Medium | Low`
- RULE_SOURCE: source rule path + section
- CODE_EVIDENCE: file path and behavior evidence
- IMPACT: risk/impact summary
- RECOMMENDATION: concrete next action

SSOT-Only Fields
- SSOT_EVIDENCE: spec evidence for mismatch

Optional Fields
- RELATED_FINDINGS: linked finding IDs
- NOTES: additional reviewer notes
