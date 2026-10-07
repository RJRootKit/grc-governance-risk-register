#!/usr/bin/env bash
# Requires: git and GitHub CLI (gh auth login). Run from this folder.
set -e
for d in grc-governance-risk-register soc2-audit-tracker-cloud-mapping vapt-threat-intel-dashboard vendor-risk-assessment-program cis-ad-security-assessment; do
  (cd "$d" && git init -q -b main && git add . && git commit -qm "Initial commit" \
   && gh repo create "$d" --public --source=. --push)
done
