# CIS / STIG Audit Method

1. Agree scope, benchmark version and authorisation.
2. Collect configuration read-only (Group Policy results, local policy export, registry checks).
3. Compare each control; record Pass / Fail / Not applicable with evidence.
4. Rate findings Critical / High / Medium / Low by exploitability and exposure.
5. For every finding record a **tested fix** and a **rollback note**.
6. Report: executive summary, score, prioritised findings, remediation plan.
7. Retest after remediation and record the new score.

Typical high-impact areas: password policy, SMB signing, firewall defaults, RDP encryption, audit policy.
