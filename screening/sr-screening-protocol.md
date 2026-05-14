# SR-01: Screening Protocol

## Overview

- **Total records for screening:** 1,132 (482 primary + 650 supplementary)
- **Reviewers:** 2 (small team)
- **Screening tool:** CSV-based tracking (records maintained in `screening-records.csv`)
- **Stages:** Title/abstract → Full-text

---

## Screening Rules

### Title/Abstract Stage Rules

1. Include if ANY of screening questions 1-3 is "Yes" or "Unclear"
2. Exclude only if ALL of questions 1-3 are "No"
3. Exclude immediately if Q5 (clearly irrelevant) is "Yes"
4. **Be LIBERAL** — over-include at this stage; specificity comes at full-text

### Full-Text Stage Rules

1. Must meet ALL eligibility criteria
2. Record ONE primary exclusion reason per excluded study
3. Each study assessed independently by both reviewers

---

## Eligibility Criteria (Quick Reference)

| Include | Exclude |
|---------|---------|
| Age ≥65 years (or subgroup data) | Age <65 without separate elderly data |
| Traumatic rib fracture(s) | Pathologic/non-traumatic fractures |
| SSRF/rib fixation (any technique) | Single-arm surgical series |
| Non-operative comparator | No comparator group |
| Reports ≥1 outcome: mortality, pneumonia, LOS, ventilation, pain, QoL | No eligible outcomes |
| RCT, cohort, case-control, before-after | Case reports (<10), reviews, editorials, animal/cadaver |
| English | Non-English full text |
| Original research | Duplicate publications |

---

## Exclusion Reason Codes (Full-Text Stage)

| Code | Reason |
|------|--------|
| WP | Wrong population |
| WI | Wrong intervention |
| NC | No eligible comparator |
| WO | Wrong outcome |
| SD | Wrong study design |
| DUP | Duplicate publication |
| ID | Insufficient data |
| CONF | Conference abstract only |
| NFT | Full text not available |
| LANG | Non-English |

---

## Pilot Screening

**Before full screening starts:**
1. Both reviewers independently screen **50 random records**
2. Compare results → calculate Cohen's κ using `scripts/kappa_calculator.py`
3. Target: κ ≥ 0.70
4. If κ < 0.60: refine criteria, re-pilot
5. If κ 0.60-0.70: brief calibration discussion, then proceed

---

## Conflict Resolution

1. Export conflicts from the screening CSV
2. Both reviewers discuss each conflict
3. Attempt consensus within 2 minutes per conflict
4. If no consensus → third reviewer (if available) or discuss with team
5. Document all conflicts and resolutions in `screening/sr-screening-conflicts.md`
6. **Batch resolution recommended** (resolve in groups of 20-30)

---

## Multiple Report Handling

- Identified by: same population, setting, recruitment period, intervention
- **Primary publication**: the one reporting the main outcome
- Link companion papers (protocols, secondary analyses) in extraction log
- Do NOT double-count participants

---

## Screening Process

1. Reviewer 1 screens all 1,132 records (title/abstract)
2. Reviewer 2 screens all 1,132 records (independently, blinded)
3. Conflicts resolved via consensus
4. Full-text PDFs retrieved for all included records
5. Both reviewers perform full-text eligibility assessment
6. Final included studies logged for Phase 5 (Extraction)

### Recommendation for the Team

Since you're a small team (2-3), I recommend:
- Use the CSV file `screening-records.csv` with separate columns for each reviewer
- Work through records in batches of **50-100 per session**
- Limit screening sessions to **2 hours** to avoid fatigue
- Track daily throughput to monitor consistency
