# Compliance Audit Tracker & SOC 2 Cloud Control Mapping

An audit findings tracker, plus a mapping of **SOC 2 Trust Services Criteria** to cloud controls, cross-referenced to **ISO 27001:2022 Annex A** so one control set serves several frameworks.

> Sample data only. Cloud examples use AWS service names; equivalents exist for Azure and GCP.

## Contents
| Path | Purpose |
|---|---|
| `templates/audit-tracker.csv` | Findings, owners, evidence, due dates |
| `templates/soc2-iso27001-cloud-mapping.csv` | TSC to cloud control to ISO mapping |
| `docs/lessons-learnt.md` | What worked and what stalled |

## Optional automation
Scan a cloud account against SOC 2 with [Prowler](https://github.com/prowler-cloud/prowler) and attach the output as evidence.
