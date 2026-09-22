# Consultant review pack: 1.2.3 Menisci

| Field | Value |
|---|---|
| Page | Menisci |
| Page id | 1.2.3 |
| Section and chapter | 1 Knee Fundamentals, 1.2 Basic Knee Anatomy |
| Page type | Anatomy |
| Tiers | Junior, Patient, Medical Student |
| Version | 1 |
| Word count | 1598, brief range 800 to 1600 |
| Style gate | Passed. Zero failures, zero warnings, template 1.0 |
| Evidence verification | **Did not run** |
| Reference list | **None** |

## What this page is

The pilot named in the AWS orchestration spec and the build order. It is the
first page produced by working the pipeline through end to end, against the
brief that shipped in the team pack and had never been used.

## How it was produced

| Stage | What happened |
|---|---|
| Brief | Loaded and validated. Governance rule confirmed: junior tier present, so commercial content refused. |
| Agent 1, writer | Run by hand against the prompt. No source retrieval was available. |
| Agent 2, fact checker | **Could not run.** No access to PubMed, Cochrane or a source library. |
| Agent 3, editor | Run by hand. The draft already met house style, so no substantive edit was made. |
| Style gate | Run for real. All thirteen rule families. Passed clean. |
| Consultant review | This pack. |

## What you are being asked to do

Return **approve**, **amend** with your edits, or **reject** with a reason.

You are doing two jobs. Confirming the anatomy, and standing in for a
verification stage that could not run at all.

**Twenty claims in this page are unverified.** Not one has been checked against
a source. They are listed in `pipeline/runs/1.2.3/draft_v1.handoff.json` under
`claims_needing_verification`. The substantive ones:

1. Medial meniscus is larger, more open in shape, and covers a smaller proportion of its tibial plateau than the lateral.
2. Medial meniscal excursion is limited by attachment to the capsule and to the deep fibres of the medial collateral ligament.
3. The lateral meniscus is separated from the capsule posterolaterally by the popliteal hiatus and is the more mobile of the two.
4. The transverse ligament connects the two anterior horns.
5. Meniscofemoral ligaments run from the posterior horn of the lateral meniscus to the medial femoral condyle.
6. Supply arises from the medial and lateral geniculate arteries through a perimeniscal capillary plexus.
7. Penetration is peripheral only, producing the red, red-white and white zones.
8. The avascular inner zone is nourished by diffusion from synovial fluid.
9. Mechanoreceptors concentrated at the horns contribute to proprioception.
10. Collagen runs in circumferential bundles with radial tie fibres, converting axial load into hoop stress.
11. Meniscal loss reduces contact area and raises peak contact stress on articular cartilage.
12. Both menisci translate posteriorly in flexion, the lateral further than the medial.
13. Composition is largely water, type one collagen dominating the dry weight.
14. Proteoglycan content is low relative to articular cartilage.
15. A small number of people have a discoid lateral meniscus.
16. Tears are found on imaging in knees that do not hurt.

## Deliberate omissions

The page gives **no numbers at all**. No proportion of load transmitted, no
prevalence for discoid meniscus, no figure for the rise in contact stress after
meniscal loss, no zone widths. Each was left out rather than estimated.

If you want a figure in any of these places, please supply the one you would
stand behind, and we will cite it when verification runs.

## Scope boundaries the brief set

The page deliberately does **not** cover:

- Detailed MRI grading. That belongs to the imaging section.
- Repair against meniscectomy decision making. That belongs to the surgery section.
- Root tear biomechanics. That belongs to 2.5.7 and 2.6.4.

Please flag anything that strays across those lines, since that is what keeps
the same material from being written repeatedly across the syllabus.

## Two sentences the editor would not touch

1. Junior tier: "A twist with the foot planted can tear one, and a torn pad spreads load less well than an intact one." Kept brief to honour the brief's outline only instruction. Is the level of detail right for reading age 12 to 14?
2. Patient tier: "A scan can show a tear in a knee that does not hurt, so the examination and the history carry as much weight as the image." Clinically loaded, written without a citation. Is the wording right?

## Scope check against the Master Publishing Architecture

The architecture arrived after this draft was written. The pilot brief carried
three exclusions. The architecture carries seven, and the draft breaches three of
the four extra ones.

| Exclusion | Owned by | Status |
|---|---|---|
| Region level anatomy detail | 2.5, 2.6 | **Overstep.** Meniscofemoral and transverse ligaments, popliteal hiatus, coronary fibres, perimeniscal plexus, geniculate supply, collagen architecture. |
| Pathology | Section 6 | **Overstep.** The patient tier describes traumatic against degenerate mechanisms. |
| Root anatomy detail | 2.5.7, 2.6.4 | **Borderline.** Roots named twice, as the anchor for hoop stress. |
| Tear classification | 6.28 to 6.33 | Clear. |
| MRI grading | 5.6.2 | Clear. Named only as a pointer. |
| Repair decisions | 7.9 | Clear. Named only as a pointer. |
| Operative treatment | Section 7 | Clear. One clause of rationale, decision pointed elsewhere. |

This is the spiral control working, not a drafting failure. The draft was written
against an incomplete brief.

**Editorial ruling needed before v2:** how much structural detail may 1.2 Basic
Knee Anatomy carry before it belongs to Section 2? The medical student tier is
the page's whole value at that level, and cutting it to bare description may
leave too little.

## Specific questions

1. Is the junior tier pitched correctly for reading age 12 to 14?
2. Does the patient tier's account of the vascular zones need more or less detail?
3. Is the medical student tier's omission of all quantitative data acceptable, or does it need figures before it is useful?
4. Does anything at a deeper tier contradict a shallower one?
5. Would you publish an anatomy page with no reference list at all, given the verification stage cannot yet run?

## Governance confirmed

- No commercial content anywhere. The brief refuses it because the junior tier is present.
- No citation markers in junior or patient text.
- Junior tier closes with the standard speak to an adult message.
- Patient tier closes with a when to seek help message.
- No em dashes, no en dashes, British English throughout.
