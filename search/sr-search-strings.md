# SR-01: Search Strings

## Database: PubMed (Primary)

**Date run:** 2026-05-14
**Hits:** 482

### String
```
(("Rib Fractures"[MeSH] OR "Flail Chest"[MeSH] OR rib fracture*[tiab]
  OR broken rib*[tiab] OR flail chest[tiab] OR chest wall injur*[tiab]
  OR "Thoracic Injuries"[MeSH])
 AND
  ("Aged"[MeSH] OR "Aged, 80 and over"[MeSH] OR elderly[tiab]
  OR older[tiab] OR geriatric[tiab] OR senior*[tiab] OR aged[tiab]
  OR older adult*[tiab] OR "65 years"[tiab] OR geriatric trauma[tiab])
 AND
  ("Fracture Fixation, Internal"[MeSH] OR "Bone Plates"[MeSH]
  OR surgical stabilization[tiab] OR rib fixation[tiab] OR rib plating[tiab]
  OR SSRF[tiab] OR internal fixation[tiab] OR operative fixation[tiab]
  OR "Conservative Treatment"[MeSH] OR non-operative[tiab]
  OR nonoperative[tiab] OR conservative management[tiab]
  OR non-surgical[tiab] OR medical management[tiab]))
```

### Notes
- Sensitivity check: 3/3 landmark papers captured
- Landmark papers tested:
  - ✅ Bulger 2000 (10866248) — Rib fractures in the elderly
  - ✅ EAST 2023 (36730672) — Non-surgical management older adults
  - ✅ Brasel 2006 (16625122) — Rib fractures pneumonia mortality

---

## Database: Cochrane CENTRAL

**Planned:** Search via cochranelibrary.com

### String (adapted)
```
#1 MeSH descriptor: [Rib Fractures] explode all trees
#2 (rib fracture* or flail chest or chest wall injur*):ti,ab,kw
#3 #1 OR #2
#4 MeSH descriptor: [Aged] explode all trees
#5 (elderly or older* or geriatric or senior* or aged):ti,ab,kw
#6 #4 OR #5
#7 (surgical stabilization or rib fixation or rib plating or SSRF):ti,ab,kw
#8 (non-operative or nonoperative or conservative or non-surgical):ti,ab,kw
#9 #7 OR #8
#10 #3 AND #6 AND #9
```

---

## Database: Scopus (EMBASE alternative)

**Planned:**

### String
```
TITLE-ABS-KEY(("rib fracture*" OR "flail chest" OR "chest wall injur*")
AND ("elderly" OR "older" OR "geriatric" OR "senior*" OR "aged")
AND ("surgical stabilization" OR "rib fixation" OR "rib plating" OR "SSRF"
OR "internal fixation" OR "operative fixation" OR "non-operative"
OR "nonoperative" OR "conservative management" OR "non-surgical"))
```

---

## Grey Literature

### ClinicalTrials.gov
**Planned search:**
```
Search: rib fracture AND (surgical stabilization OR rib fixation OR SSRF)
```

### WHO ICTRP
**Planned search:**
```
Search: rib fracture AND surgical
```
