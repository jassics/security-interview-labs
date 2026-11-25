#!/usr/bin/env python3
"""Summarise market-data/postings.csv for interview prep.

Prints skill shares (not absolute counts) by archetype and level band, and the
spread of employer-posted pay ranges. Standard library only.

    python3 analyze.py                 # plain text
    python3 analyze.py --markdown      # tables you can paste into the book
    python3 analyze.py --family product_security
"""
import argparse
import csv
import statistics
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path

HERE = Path(__file__).parent
STALE_DAYS = 365
MIN_GROUP = 5  # below this many postings a share is too noisy to print


def load(path=HERE / "postings.csv"):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def load_taxonomy(path=HERE / "taxonomy.csv"):
    with open(path, newline="") as f:
        return {r["skill_id"]: r["label"] for r in csv.DictReader(f)}


def skills_of(row):
    return [s for s in row["skills"].split(";") if s]


def skill_shares(rows):
    """Return {skill: share of postings in rows that mention it}."""
    if not rows:
        return {}
    counts = Counter(s for r in rows for s in set(skills_of(r)))
    return {s: c / len(rows) for s, c in counts.items()}


def group_by(rows, key):
    groups = defaultdict(list)
    for r in rows:
        groups[r[key]].append(r)
    return groups


def pay_spread(rows):
    """Median low and median high of posted ranges, per (currency, level_band)."""
    out = {}
    buckets = defaultdict(list)
    for r in rows:
        if r["pay_min"] and r["pay_max"]:
            buckets[(r["currency"], r["level_band"])].append((float(r["pay_min"]), float(r["pay_max"])))
    for key, pairs in buckets.items():
        out[key] = (len(pairs), statistics.median(p[0] for p in pairs), statistics.median(p[1] for p in pairs))
    return out


def stale_rows(rows, today=None, days=STALE_DAYS):
    today = today or date.today()
    old = []
    for r in rows:
        seen = datetime.strptime(r["accessed"], "%Y-%m-%d").date()
        if (today - seen).days > days:
            old.append(r)
    return old


def pct(x):
    return f"{round(x * 100):d}%"


def top_skills(rows, taxonomy, n=6):
    shares = skill_shares(rows)
    ranked = sorted(shares.items(), key=lambda kv: (-kv[1], kv[0]))[:n]
    return [(taxonomy.get(s, s), v) for s, v in ranked]


def render(rows, taxonomy, markdown=False):
    lines = []
    h = (lambda t: f"\n### {t}\n") if markdown else (lambda t: f"\n== {t} ==")
    lines.append(f"Sample: {len(rows)} postings, {len({r['company'] for r in rows})} companies")

    lines.append(h("Most common skills overall (share of postings)"))
    for label, v in top_skills(rows, taxonomy, 10):
        lines.append(f"- {label}: {pct(v)}" if markdown else f"  {label:<45}{pct(v):>5}")

    lines.append(h("By company archetype"))
    for arch, grp in sorted(group_by(rows, "archetype").items()):
        if len(grp) < MIN_GROUP:
            lines.append(f"- {arch}: only {len(grp)} postings, not summarised")
            continue
        top = ", ".join(f"{l} {pct(v)}" for l, v in top_skills(grp, taxonomy))
        lines.append(f"- {arch} (n={len(grp)}): {top}")

    lines.append(h("By level band"))
    for band in ("entry", "mid", "senior", "staff_plus", "manager"):
        grp = [r for r in rows if r["level_band"] == band]
        if len(grp) < MIN_GROUP:
            lines.append(f"- {band}: only {len(grp)} postings, not summarised")
            continue
        top = ", ".join(f"{l} {pct(v)}" for l, v in top_skills(grp, taxonomy))
        lines.append(f"- {band} (n={len(grp)}): {top}")

    lines.append(h("Employer-posted pay ranges (median of lows to median of highs)"))
    spread = pay_spread(rows)
    if not spread:
        lines.append("- none")
    for (cur, band), (n, lo, hi) in sorted(spread.items()):
        flag = " [indicative only, n<3]" if n < 3 else ""
        lines.append(f"- {cur} {band} (n={n}): {lo:,.0f} to {hi:,.0f} per year{flag}")
    no_pay = sum(1 for r in rows if not r["pay_min"])
    lines.append(f"\n{no_pay} of {len(rows)} postings published no pay range.")
    india = [r for r in rows if "India" in r["location"] or r["location"] in ("Bengaluru", "Bangalore")]
    if india and not any(r["pay_min"] for r in india):
        lines.append("None of the India-based postings published pay; use compensation.csv aggregates for INR.")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--csv", default=str(HERE / "postings.csv"))
    ap.add_argument("--family", help="filter by role_family, for example product_security")
    ap.add_argument("--markdown", action="store_true")
    args = ap.parse_args()

    rows = load(args.csv)
    if args.family:
        rows = [r for r in rows if r["role_family"] == args.family]
    old = stale_rows(rows)
    if old:
        print(f"WARNING: {len(old)} rows were accessed more than {STALE_DAYS} days ago; refresh before quoting.\n")
    print(render(rows, load_taxonomy(), args.markdown))


if __name__ == "__main__":
    main()
