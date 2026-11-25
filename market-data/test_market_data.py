"""Guards that keep the dataset honest: every row needs a source and a date,
ranges must be ordered, and skill tags must exist in the taxonomy."""
import csv
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

import analyze

HERE = Path(__file__).parent
POSTINGS = analyze.load()
TAXONOMY = analyze.load_taxonomy()
LEVELS = {"entry", "mid", "senior", "staff_plus", "manager", "unspecified"}
SOURCE_TYPES = {"official", "mirror"}
FAMILIES = {"product_security", "cloud_infra_security", "detection_response", "security_tooling",
            "offensive", "leadership_grc", "other_security"}
REQUESTED_COMPANIES = {"Flipkart", "Amazon", "Stripe", "eBay", "Rippling", "Sarvam AI", "Anthropic", "Coupang",
                       "Meesho", "PhonePe", "Walmart", "Harness", "Avalara", "Meta", "Circle", "Wind River",
                       "Razorpay", "Slice", "Zepto", "Gainsight", "CRED", "Swiggy", "Tesco", "Cisco", "Arctic Wolf",
                       "Atlassian", "Okta", "Salesforce", "Adobe", "Google", "Microsoft"}


def test_every_requested_company_is_present():
    assert {r["company"] for r in POSTINGS} == REQUESTED_COMPANIES


def test_rows_have_source_and_date():
    for r in POSTINGS:
        assert r["source_url"].startswith("https://"), r["role_title"]
        assert r["source_type"] in SOURCE_TYPES, r["role_title"]
        accessed = datetime.strptime(r["accessed"], "%Y-%m-%d").date()
        assert accessed <= date.today(), r["role_title"]


def test_enums_and_skills_are_valid():
    for r in POSTINGS:
        assert r["level_band"] in LEVELS, r["role_title"]
        assert r["role_family"] in FAMILIES, r["role_title"]
        tags = analyze.skills_of(r)
        assert tags, r["role_title"]
        for t in tags:
            assert t in TAXONOMY, f"{t} in {r['role_title']}"


def test_pay_ranges_are_ordered_and_sourced():
    for r in POSTINGS:
        if r["pay_min"] or r["pay_max"]:
            assert r["pay_min"] and r["pay_max"], r["role_title"]
            assert float(r["pay_min"]) <= float(r["pay_max"]), r["role_title"]
            assert r["currency"] in {"USD", "EUR", "INR", "CAD"}, r["role_title"]
            assert r["pay_period"] == "year", r["role_title"]
            assert r["pay_source_url"].startswith("https://"), r["role_title"]
        else:
            assert not r["currency"] and not r["pay_source_url"], r["role_title"]


def test_no_duplicate_rows():
    keys = [(r["company"], r["role_title"], r["location"], r["source_url"]) for r in POSTINGS]
    assert len(keys) == len(set(keys))


def test_compensation_rows_are_dated_and_sourced():
    with open(HERE / "compensation.csv", newline="") as f:
        rows = list(csv.DictReader(f))
    assert rows
    for r in rows:
        if r["source"] == "practitioner_reported":
            assert "not a public statistic" in r["notes"]
        else:
            assert r["source_url"].startswith("https://")
        assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", r["as_of_seen"])
        assert r["currency"] in {"USD", "INR", "EUR"}
        if r["low"] and r["high"]:
            assert float(r["low"]) <= float(r["high"])
        assert r["low"] or r["high"] or r["value"]


def test_analyze_runs():
    out = subprocess.run([sys.executable, str(HERE / "analyze.py"), "--markdown"],
                         capture_output=True, text=True, check=True).stdout
    assert "Most common skills overall" in out


def test_staleness_check_flags_old_rows():
    old = analyze.stale_rows(POSTINGS, today=date(2028, 1, 1))
    assert len(old) == len(POSTINGS)
    assert analyze.stale_rows(POSTINGS, today=date(2026, 12, 1)) == []


def test_tags_basis_is_declared():
    assert all(r["tags_basis"] in {"full_text", "snippet"} for r in POSTINGS)
