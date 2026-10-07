#!/usr/bin/env python3
"""Rank vulnerability findings by threat-informed priority.

Usage: prioritise.py findings.csv assets.csv > priority.csv
priority = cvss + 2*known_exploited + 1*exploit_available
           + 0.5*criticality(1-5) + 1*internet_facing
"""
import csv
import sys


def yes(v):
    return str(v).strip().lower() in ("yes", "y", "true", "1")


def load_assets(path):
    with open(path, newline="") as f:
        return {r["host"]: r for r in csv.DictReader(f)}


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    assets = load_assets(sys.argv[2])
    rows = []
    with open(sys.argv[1], newline="") as f:
        for r in csv.DictReader(f):
            a = assets.get(r["host"], {"criticality": "3", "internet_facing": "no"})
            score = (
                float(r["cvss"])
                + 2 * yes(r["known_exploited"])
                + 1 * yes(r["exploit_available"])
                + 0.5 * float(a["criticality"])
                + 1 * yes(a["internet_facing"])
            )
            r["priority_score"] = round(score, 1)
            rows.append(r)
    rows.sort(key=lambda x: x["priority_score"], reverse=True)
    out = csv.DictWriter(sys.stdout, fieldnames=list(rows[0].keys()))
    out.writeheader()
    out.writerows(rows)


if __name__ == "__main__":
    main()
