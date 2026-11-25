# market-data: what security roles ask for, and what they pay

A small, dated dataset behind the front matter of the *Product Security Interview Playbook*. It covers 31 companies: Flipkart, Amazon, Stripe, eBay, Rippling, Sarvam AI, Anthropic, Coupang, Meesho, PhonePe, Walmart, Harness, Avalara, Meta, Circle, Wind River, Razorpay, Slice, Zepto (India quick commerce), Gainsight, CRED, Swiggy, Tesco, Cisco, Arctic Wolf, Atlassian, Okta, Salesforce, Adobe, Google and Microsoft.

**Design rule: the book teaches skills that last; this folder holds the numbers that expire.** Every figure carries a source URL and the date it was seen. Pay is always a range, never a single promised number. The book quotes shares and ranks, not headline salaries, and links here for the dated detail.

## Files

| File | What it holds |
|---|---|
| `postings.csv` | One row per public security job posting: company, archetype, role family, level band, location, source URL, source type, date accessed, pay range if the employer published one, skill tags |
| `compensation.csv` | Aggregate pay references (levels.fyi, Payscale, Salary.com) with the date seen and the date the page says it was updated |
| `taxonomy.csv` | The skill tags, each mapped to a chapter of the book |
| `analyze.py` | Skill shares by archetype and level band, and the spread of posted pay ranges. `--markdown` prints paste-ready tables |
| `test_market_data.py` | Checks that every row has a source and a date, ranges are ordered, and tags exist in the taxonomy |

Run it:

```bash
python3 analyze.py                      # all rows
python3 analyze.py --family product_security --markdown
python3 -m pytest -q                    # data checks
```

## Snapshot: 25 November 2026

- 131 postings across 31 companies.
- 20 postings published a pay range; 59 did not. All 20 are US or Ireland roles.
- No India-based posting published pay. For INR, use the aggregates in `compensation.csv` and treat them as order of magnitude.
- The skill mix that stands out: security architecture and design review dominates staff-and-above roles; cloud security and CI/CD and secure-SDLC dominate fintech and SaaS postings; AI and LLM security now appears in roughly one posting in five, and more often at the staff level.

## How to read the numbers

- **Source type.** `official` means the employer's own careers or applicant-tracking page. `mirror` means a job board that reproduces the employer's posting. Mirrors can lag or drop details, so prefer `official` rows when quoting.
- **Pay ranges.** US employers in some states must publish a range, so those are the ones captured. A range is usually base pay and excludes equity and bonus, but the posting is the authority; check it before quoting. Walmart and Amazon ranges span geographic markets.
- **Outliers stay visible.** Two Harness rows carry the same title with very different ranges; the note column says so. Do not average them without looking.
- **Small groups.** Anything under 5 postings is not summarised by skill, and pay groups under 3 are marked indicative.
- **Levels.fyi and similar sites** are crowdsourced and noisy at the company level. They are context for a negotiation conversation, not a quote.

## Limits you should know about

- **Skill tags are mixed in quality.** The `tags_basis` column says `full_text` (64 postings, tagged from the fetched page) or `snippet` (67 postings, tagged from page excerpts and search snippets). The snippet-tagged ones could not be fetched in full (dead or redirected pages, blocked job boards), or were added after the full-text pass. Treat the shares as a directional signal and the ranks as more trustworthy than the exact percentages. Finishing the full-text pass is the first thing to do on the next refresh.
- The sample is what public search surfaced on one day, not a census of each company's openings, and some companies are represented by only a few roles.
- Postings close and move. Rows record that a role was public on the access date, nothing more.
- Levels.fyi was not opened directly in this pass. The figures here are the aggregate numbers shown in its public search listings, attributed below.

## Refresh method (about two hours, twice a year)

1. For each company, search its careers page or applicant-tracking page for product security, application security, cloud security and security architecture roles.
2. Add new rows; do not edit old rows except to fix a mistake. Set `accessed` to the day you saw the posting.
3. Read the full description for each new row and tag from the full text. Add a tag to `taxonomy.csv` only if three or more postings need it.
4. Record pay only when the employer or an exact mirror shows a range. Put the page you read it from in `pay_source_url`.
5. Run `python3 -m pytest -q`, then `python3 analyze.py --markdown` and update the numbers in the book front matter. `analyze.py` warns when rows are older than 12 months.
6. Anything not seen in two refreshes in a row can be moved to `archive/` so the dataset stays current.

## Attribution and takedown

Levels.fyi figures are credited to Levels.fyi (https://www.levels.fyi) and used here as a few aggregate numbers for context. Payscale and Salary.com figures are credited to those sites. Job posting text is not copied; the dataset stores titles, links and tags only. If a company or site would like a row changed or removed, open an issue and it will be removed.
