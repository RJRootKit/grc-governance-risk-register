# Vulnerability Assessment, Pentest & Threat-Informed Prioritisation

Templates and a small Python tool for scoping tests, triaging findings, and producing a threat-informed patch priority list.

> **Authorised testing only.** Never scan or test systems without written permission. Sample data is fictional.

## Contents
| Path | Purpose |
|---|---|
| `docs/scope-and-roe-template.md` | Scope and rules of engagement |
| `templates/pentest-report-template.md` | Report structure |
| `tools/prioritise.py` | Ranks findings by CVSS, exploitability, known-exploited status and asset criticality |
| `sample-data/` | Example inputs |

## Run
```bash
python3 tools/prioritise.py sample-data/findings.csv sample-data/assets.csv > priority.csv
```
Export your own scanner results (for example Nessus CSV) into the `findings.csv` column layout.

## Method note
Prioritise by exploitability and asset criticality, not CVSS alone. Raw scanner output always needs triage.
