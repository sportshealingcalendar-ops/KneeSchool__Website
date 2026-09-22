# KneeSchool Master Publishing Architecture

Part 1 of 6: whole syllabus structure, plus the full page map for Sections 0 to 3.
Version 1.0. 22 September 2026. Owner: Editor in Chief.

---

## 1. Purpose and Authority

This document is the definitive page map of KneeSchool. It exists so that the content pipeline can run its first instruction on every page: locate the page, read its neighbours, and identify what the page must not cover. It also seeds the article tracker.

Authority boundaries:

- The Operations Handbook governs article structure, editorial standards and QA. This document does not restate them.
- This document governs page numbering, page scope, tier coverage per page, spiral linkage, page types and build priority. Where any other document names a different scope or number for a page, this document wins.
- The companion JSON file (kneeschool_architecture_pages_sections_0_to_3.json) is generated from the same data as the page map in this document. Regenerate the tracker from the JSON; never hand edit the two apart.

## 2. Numbering and Reading Conventions

- Page ids are section.chapter.page, for example 1.2.3 Menisci and 2.7.6 Femoral Footprint of the ACL. Chapter ids are section.chapter.
- The Parts used inside large sections (Part A, Part B and so on in Sections 6 to 15) are navigational groupings only. They never appear in page ids.
- In deeper_pages and must_not_cover, an id with two components (for example 3.6) refers to a whole chapter; three components refer to one page.
- Siblings are the other pages of the same chapter, listed in full in the JSON.
- A chapter listed in the source architecture without numbered sub pages (common from Section 6 onwards) publishes as a single page carrying the chapter id, unless its instalment of this document splits it. Sub items listed without numbers in the source (for example the repair variants under 7.14) receive numbered ids in their instalment.
- Source titles are normalised to British English where needed (2.12.5 Dynamic Stabilisers); ids are unchanged.

## 3. The Seven Tiers

Junior, Patient, Medical Student, MRCS, FRCS (Tr and Orth), Fellowship, Consultant. Section 0 Junior Academy was added below Patient after the original architecture was drafted; this document is the first to integrate it. Tier registers, headings and block rules are defined in the Operations Handbook. Each page's tiers_required lists the tier blocks that page carries; tier sets in Part 1 are editorial defaults awaiting Editor in Chief sign off (Open Questions).

## 4. Section Catalogue

Sixteen sections. Estimated page counts for Sections 4 to 15 are the source architecture's own estimates; their full page maps follow in later instalments.

**Section 0: Junior Academy** (38 pages, mapped in full below). Pre university tier for school age learners, teachers, coaches and parents. Chapters 0.1 Discover the Knee, 0.2 Sport and Your Knees, 0.3 Careers in Knee Medicine, 0.4 Getting Into Medical School, 0.5 Young Investigators, 0.6 Junior Certificates and Challenges, 0.7 For Teachers, Coaches and Parents. Binding governance: no commercial content anywhere in Section 0, no clinical advice, reading age 12 to 14, pre-moderated interactivity, UK GDPR and the ICO Age Appropriate Design Code, named safeguarding lead.

**Section 1: Knee Fundamentals** (16 pages, mapped in full below). The shallow entry point of the spiral for Junior, Patient and Medical Student tiers. Chapters 1.1 Introduction to the Knee, 1.2 Basic Knee Anatomy.

**Section 2: Anatomy Academy** (79 pages, mapped in full below). Structure by structure anatomy for professional tiers. Chapters 2.1 Femur, 2.2 Tibia, 2.3 Fibula, 2.4 Patella, 2.5 Medial Meniscus, 2.6 Lateral Meniscus, 2.7 ACL, 2.8 PCL, 2.9 Medial Structures, 2.10 Lateral Structures, 2.11 Rotational Structures, 2.12 Patellofemoral Anatomy.

**Section 3: Biomechanics Academy** (188 pages, mapped in full below). Chapters 3.1 Introduction through 3.17 Landmark Biomechanics Papers, spanning motion, kinematics, kinetics, contact mechanics, structure specific biomechanics, alignment, gait, sport and advanced methods.

**Section 4: Clinical Examination Academy** (estimated 150 to 200 pages). Examination for Medical Student to Fellowship tiers, with strong video and OSCE and viva value. Chapters 4.1 to 4.24: introduction, history taking, inspection, gait, alignment, palpation, range of motion, effusion, then structure specific examination (4.9 meniscal to 4.15 patellofemoral), tendons, cartilage, osteoarthritis, paediatric, post operative, functional testing, scoring systems, special situations, landmark papers.

**Section 5: Imaging Academy** (estimated 250 to 350 pages). Physics, radiographs, ultrasound, MRI protocols and normal anatomy, then structure specific MRI (5.6 meniscal to 5.12 patellofemoral), bone and marrow, synovial disorders, paediatric MRI, CT, post operative imaging, advanced imaging, the Magic Angle MRI Academy (5.19), reporting (5.20) and landmark papers (5.21).

**Section 6: Conditions Library** (estimated 500 to 700 pages). The clinical core, chapters 6.1 to 6.156 across Parts A to T: ACL disorders (6.1 to 6.8), PCL (6.9 to 6.13), medial (6.14 to 6.20), lateral (6.21 to 6.26), meniscal (6.27 to 6.43), cartilage (6.44 to 6.52), patellofemoral (6.53 to 6.63), tendon (6.64 to 6.70), osteoarthritis (6.71 to 6.80), inflammatory (6.81 to 6.87), paediatric (6.88 to 6.95), fractures (6.96 to 6.101), bone and marrow (6.102 to 6.107), tumours (6.108 to 6.116), synovial (6.117 to 6.120), infection (6.121 to 6.126), special populations (6.127 to 6.134), complex knee (6.135 to 6.140), conditions by symptom (6.141 to 6.148), landmark papers and controversies (6.149 to 6.156).

**Section 7: Surgical Academy** (estimated 450 to 600 pages). Chapters 7.1 to 7.136 across Parts A to R: principles (7.1 to 7.4), arthroscopy (7.5 to 7.7), meniscal surgery (7.8 to 7.19), ACL surgery (7.20 to 7.31), PCL (7.32 to 7.37), medial (7.38 to 7.44), lateral (7.45 to 7.50), patellofemoral (7.51 to 7.57), cartilage restoration (7.58 to 7.67), osteotomy (7.68 to 7.75), arthroplasty (7.76 to 7.88), paediatric (7.89 to 7.94), multi ligament (7.95 to 7.100), biologics (7.101 to 7.106), complications (7.107 to 7.113), surgical education (7.114 to 7.120), masterclasses (7.121 to 7.128), landmark papers (7.129 to 7.136).

**Section 8: Rehabilitation Academy** (estimated 300 to 450 pages). Chapters 8.1 to 8.115: principles and tissue healing, foundations, procedure specific rehabilitation (ACL 8.8 to 8.13, meniscal 8.14 to 8.19, PCL, collaterals, patellofemoral, cartilage, osteotomy, arthroplasty), sports performance, injury prevention, functional testing, technology, nutrition, sleep, psychology, special populations, the Sportshealing rehabilitation system (8.104 to 8.108), landmark papers.

**Section 9: Women's Knee Health Academy** (estimated 250 to 400 pages). Chapters 9.1 to 9.79: foundations, puberty, menstrual cycle, the female athlete ACL programme, RED-S, pregnancy, postpartum, perimenopause, menopause, HRT, nutrition, female specific conditions, women's sports, elite programmes, clinic pathways, research, the OmKneeHealth women's hub (9.69 to 9.73), masterclasses.

**Section 10: Children's Knee Health Academy** (estimated 250 to 350 pages). Chapters 10.1 to 10.94: the growing knee, paediatric examination, sports injuries, the paediatric ACL programme, meniscal disorders, OCD, patellofemoral, traction apophysitis, alignment, fractures, tumours, infection, rehabilitation, young athlete programme, parents' education centre (10.62 to 10.69), prevention, clinic pathways, research, masterclasses.

**Section 11: Performance and Injury Prevention Academy** (estimated 300 to 500 pages). Chapters 11.1 to 11.83: performance foundations, movement assessment, strength, power, running, agility, ACL prevention (11.21 to 11.27), sport specific performance, female athletes, youth development, recovery science, nutrition, technology, elite athlete centre, the Sportshealing performance centre, research, masterclasses.

**Section 12: Research Academy** (estimated 250 to 400 pages). Chapters 12.1 to 12.62: research foundations, methodology, biostatistics, critical appraisal, systematic reviews, clinical research, biomechanics research, imaging research, surgical education research, writing and publishing, grants and careers, topic research hubs (ACL 12.33, meniscus 12.34, medial 12.35 to 12.38, arthroplasty 12.39 to 12.42), research database, AI and future research, masterclasses.

**Section 13: Case Library** (large; a mature library exceeds 1,000 cases). Chapters 13.1 to 13.66: clinical reasoning, then case sets by topic (ACL 13.3 to 13.5, meniscal, medial, lateral, PCL, cartilage, patellofemoral, osteoarthritis, paediatric, sport), imaging challenges (13.28 to 13.32), surgical decision making, complications, FRCS viva cases (13.41 to 13.46), fellowship challenges, consultant mastercases, Sportshealing grand rounds, the global case registry.

**Section 14: Question Bank and Examination Academy** (very large; the mature bank targets tens of thousands of questions). Chapters 14.1 to 14.80: quiz and question banks per tier (patient 14.1 to 14.2, medical student 14.3 to 14.5, MRCS 14.6 to 14.9, FRCS 14.10 to 14.14, viva 14.15 to 14.18, fellowship 14.19 to 14.20), topic banks (14.21 to 14.37), decision making (14.38 to 14.40), rapid review (14.41 to 14.46), board courses (14.47 to 14.50), interactive learning (14.51 to 14.53), CPD (14.54 to 14.58), certification programmes (14.59 to 14.62), diplomas (14.63 to 14.68), examination masterclasses (14.69 to 14.74), analytics (14.75 to 14.80).

**Section 15: Video Academy** (estimated 1,000 to 2,000 videos at maturity). Chapters 15.1 to 15.100: introduction series, patient education, anatomy, biomechanics, examination, imaging including the Magic Angle series (15.22), surgical videos (15.23 to 15.29), rehabilitation, women's and children's series, performance, case videos, fellowship masterclasses (15.55 to 15.61), research videos, podcasts, the Sportshealing channel, KneeSchool TV, premium content, video certification, future development.

## 5. Spiral Linkage Map

The chain each core topic follows, shallowest to deepest. Every page in a chain lists its own neighbours and owners in the page map; this table is the whole syllabus view. Ids with two components are chapters.

| Topic | Spiral chain, shallowest to deepest |
|---|---|
| Meniscus | 0.1.2 → 1.2.3 → 2.5 and 2.6 → 3.6 → 4.9 → 5.6 → 6.27 to 6.43 → 7.8 to 7.19 → 8.14 to 8.19 → 12.34 → 13.6 and 13.7 → 14.22 and 14.43 → 15.7, 15.12, 15.24 |
| ACL | 0.2.4 → 1.2.4 → 2.7 → 3.7 → 4.10 → 5.7 → 6.1 to 6.8 → 7.20 to 7.31 → 8.8 to 8.13 → 12.33 → 13.3 to 13.5 → 14.23 and 14.42 → 15.3, 15.11, 15.16, 15.25 |
| PCL | 1.2.4 → 2.8 → 3.8 → 4.11 → 5.8 → 6.9 to 6.13 → 7.32 to 7.37 → 8.20 to 8.24 → 13.11 → 14.24 |
| Medial knee | 1.2.4 → 2.9 → 3.9 → 4.12 → 5.9 → 6.14 to 6.20 → 7.38 to 7.44 → 8.25 to 8.26 → 12.35 to 12.38 → 13.8 and 13.9 → 14.25 → 15.13, 15.26 |
| Lateral and PLC | 1.2.4 → 2.10 → 3.10 → 4.13 → 5.10 → 6.21 to 6.26 → 7.45 to 7.50 → 8.27 → 13.10 → 14.26 |
| Anterolateral complex | 2.11 → 3.11 → 4.14 → 6.100 → 7.30 → 13.5.3 |
| Patellofemoral | 1.2.1 → 2.4 and 2.12 → 3.12 → 4.15 → 5.12 → 6.53 to 6.63 → 7.51 to 7.57 → 8.29 to 8.33 → 13.14 and 13.15 → 14.27 → 15.9, 15.27 |
| Cartilage | 1.2.2 → 3.5 → 4.17 → 5.11 → 6.44 to 6.52 → 7.58 to 7.67 → 8.34 to 8.39 → 13.12 and 13.13 |
| Osteoarthritis and arthroplasty | 1.1.5 → 3.13 → 4.18 → 5.3.4 → 6.71 to 6.80 → 7.76 to 7.88 → 8.44 to 8.48 → 12.39 to 12.42 → 13.16 to 13.18 → 14.44 and 14.45 → 15.5, 15.29 |
| Osteotomy | 3.13 → 5.16.5 → 7.68 to 7.75 → 8.40 to 8.43 → 13.48 → 15.28 |
| Paediatric knee | 0.1.5 → 1.2.10 → 4.19 → 5.15 → 6.88 to 6.95 → 7.89 to 7.94 → 8.98 → Section 10 → 13.19 to 13.21 → 14.13 → 15.40 to 15.44 |
| Women's knee health | 0.2.4 → 3.7.15 → 6.6 and 6.127 to 6.130 → 8.99 and 8.100 → Section 9 → 13.15.3 → 14.67 → 15.35 to 15.39 |
| Examination | 4.1 to 4.24 → 13.41 (viva) → 14.15 → 15.14 to 15.17 |
| Imaging | 0.7.4 in outline → 5.1 to 5.21 → 13.28 to 13.32 → 14.34 to 14.37 → 15.18 to 15.22 |
| Rehabilitation and return to sport | 0.2.3 → 8.1 to 8.115 → 11 Parts A to G → 13.60 → 14.62 → 15.30 to 15.34 |
| Research | 0.5 → 3.17 and other landmark chapters → Section 12 → 15.62 to 15.66 |
| Careers and examinations | 0.3 and 0.4 → 7.114 to 7.120 → 12.31 and 12.32 → 14.69 to 14.74 |

## 6. Page Types

The fine grained page_type carried in the JSON, and the Operations Handbook article template each maps to. Types marked (variant pending) map to the nearest template today and are candidates for their own template in Handbook v1.1.

| page_type | Used for | Template mapping |
|---|---|---|
| anatomy | Sections 1.2 and 2 | anatomy |
| biomechanics | Section 3 | anatomy (variant pending) |
| condition | Section 6 and condition style pages elsewhere | condition |
| procedure | Section 7 operative pages | procedure |
| examination | Section 4 | anatomy (variant pending) |
| imaging | Section 5 | anatomy (variant pending) |
| rehabilitation | Section 8 | condition (variant pending) |
| foundations | Section 1.1 and section introductions | anatomy |
| junior_explainer | Section 0 teaching pages | anatomy, junior framing |
| careers, study_skills, teacher_resource | Section 0 chapters 0.3 to 0.7 | anatomy skeleton, junior careers framing (variant pending) |
| landmark_papers | Landmark chapters in every section | anatomy (variant pending) |
| assessment | Certificates, quizzes, question pages | owned by Section 14 conventions (variant pending) |
| case, video | Sections 13 and 15 | defined in their instalments |

## 7. Build Sequence and Priority

Priorities in the JSON follow the 18 month roadmap. The tracker queue is: all high pages in section order, then medium, then low; within a band, lower page id first.

| Phase | Months | Architecture scope | Priority effect |
|---|---|---|---|
| Foundation | 1 to 3 | Section 1 in full; high priority anatomy and biomechanics (2.5, 2.6, 2.7, 2.9, 2.12, 3.6, 3.7) | The 90 high priority pages in this instalment are the Foundation queue, matching the 100 page target |
| Core build | 4 to 6 | Rest of Sections 2 and 3; Section 0 (reuses Section 1 assets); Section 4 and Section 5 core | Medium priority in Sections 0, 2, 3; Section 4 and 5 priorities arrive in Part 2 |
| Conditions | 7 to 9 | Section 6; Sections 9 and 10 cores | Part 3 instalment |
| Surgery | 10 to 12 | Section 7; Sections 8 and 11 cores | Part 4 and Part 5 instalments |
| Research | 13 to 15 | Section 12; landmark chapters across sections (3.17, 5.21 and peers) | Landmark chapters are low priority until this phase |
| Advanced | 16 to 18 | Sections 13, 14, 15 | Part 6 instalment |

## 8. Page Count Summary, This Instalment

| Section | Pages | High | Medium | Low |
|---|---|---|---|---|
| 0 | 38 | 2 | 26 | 10 |
| 1 | 16 | 16 | 0 | 0 |
| 2 | 79 | 38 | 38 | 3 |
| 3 | 188 | 34 | 134 | 20 |
| Total | 321 | 90 | 198 | 33 |

Siblings are recorded in full in the JSON; in the page map below they are implied (all other pages of the same chapter). Chapter defaults apply to every page in the chapter; a page's bracketed notes list only its additions or overrides.

---

# Full Page Map: Sections 0 to 3

## Section 0: Junior Academy


### Chapter 0.1 Discover the Knee

Defaults for this chapter. Tiers: junior. Page type: junior_explainer. Priority: medium. Deeper spiral: 1.1; 1.2. Chapter level must not cover: Diagnosis or treatment advice at any depth (Sections 4 to 8 own clinical content) | Commercial content of any kind (prohibited across Section 0).

- **0.1.1 Meet Your Knee.** An illustrated first tour of the knee joint and its parts. (Priority: high. Also deeper: 1.1.1)
- **0.1.2 Bones, Ligaments, Menisci and Muscles.** The four building blocks of the knee, simply explained. (Also must not cover: Formal anatomy detail (owned by 1.2 and Section 2). Also deeper: 1.2.1; 1.2.3; 1.2.4; 1.2.6)
- **0.1.3 How the Knee Moves.** Hinges, rolling and gliding described in plain terms. (Also must not cover: Kinematics terminology and analysis (owned by 3.3). Also deeper: 3.2; 3.3)
- **0.1.4 The Knee Under Load.** Forces in walking, running and jumping, introduced simply. (Also must not cover: Kinetics detail (owned by 3.4). Also deeper: 3.4)
- **0.1.5 Growing Knees.** Growth plates and why young knees are different. (Also must not cover: Physeal injury management (owned by 10.39 and 10.40). Also deeper: 1.2.10; 10.2)
- **0.1.6 Curriculum Links.** Mapping to GCSE and A level biology and PE topics. (Type: teacher_resource)

### Chapter 0.2 Sport and Your Knees

Defaults for this chapter. Tiers: junior. Page type: junior_explainer. Priority: medium. Deeper spiral: 10.6; 11.2. Chapter level must not cover: Diagnosis or treatment advice at any depth (Sections 4 to 8 own clinical content) | Commercial content of any kind (prohibited across Section 0).

- **0.2.1 Common Knee Injuries in Young Athletes.** Recognition in outline, never self diagnosis. (Also must not cover: Imaging appearances (owned by 5.15). Also deeper: 6.88; 10.7; 10.8)
- **0.2.2 Osgood-Schlatter and Growing Pains.** What they are and why they usually settle. (Also deeper: 6.67; 10.26)
- **0.2.3 Warm-Ups That Work.** Evidence supported prevention programmes described simply. (Also must not cover: Programme prescription detail (owned by 11.22). Also deeper: 8.61; 11.22)
- **0.2.4 Girls, Boys and Knees.** Why ACL risk differs between sexes, introduced simply. (Also deeper: 6.6; 9.10; 11.37)
- **0.2.5 When to Tell an Adult.** Warning signs framed as speak to a professional. (Also must not cover: Clinical red flag pathways (owned by 10.4.5). Also deeper: 10.63)
- **0.2.6 Athlete Stories.** Real injury and recovery journeys told for young readers.

### Chapter 0.3 Careers in Knee Medicine

Defaults for this chapter. Tiers: junior. Page type: careers. Priority: medium. Deeper spiral: 7.119; 7.120. Chapter level must not cover: Diagnosis or treatment advice at any depth (Sections 4 to 8 own clinical content) | Commercial content of any kind (prohibited across Section 0).

- **0.3.1 The Road to Knee Surgeon.** Interactive pathway map from school to consultant. (Priority: high. Also deeper: 14.69; 14.73)
- **0.3.2 A Day in the Life.** Profiles across the knee care team, surgeon to researcher.
- **0.3.3 Beyond Surgery.** Physiotherapy, radiography, sports science and allied careers.
- **0.3.4 What MRCS and FRCS Actually Are.** The surgical examinations demystified for school readers. (Also deeper: 14.70; 14.71)
- **0.3.5 Women in Orthopaedics.** Role models and representation in the specialty. (Also deeper: 15.68)
- **0.3.6 Ask a Surgeon.** Pre-moderated question and answer archive. (Priority: low)

### Chapter 0.4 Getting Into Medical School

Defaults for this chapter. Tiers: junior. Page type: study_skills. Priority: medium. Deeper spiral: none recorded. Chapter level must not cover: Diagnosis or treatment advice at any depth (Sections 4 to 8 own clinical content) | Commercial content of any kind (prohibited across Section 0).

- **0.4.1 Choosing Subjects.** A level and equivalent requirements for medicine.
- **0.4.2 Work Experience and Volunteering.** What counts and how to reflect on it.
- **0.4.3 UCAT and Admissions Tests.** Orientation only, signposting official resources. (Also must not cover: Test coaching content (out of platform scope; signpost official sources))
- **0.4.4 Personal Statements and Interviews.** Using an interest in orthopaedics well.
- **0.4.5 Widening Participation.** Routes, bursaries and support for under represented students.
- **0.4.6 Gateway and Graduate Entry Routes.** Alternative entry routes into medicine.

### Chapter 0.5 Young Investigators

Defaults for this chapter. Tiers: junior. Page type: study_skills. Priority: medium. Deeper spiral: 12.1. Chapter level must not cover: Diagnosis or treatment advice at any depth (Sections 4 to 8 own clinical content) | Commercial content of any kind (prohibited across Section 0).

- **0.5.1 How We Know What We Know.** Evidence in medicine introduced for school readers. (Also deeper: 12.4)
- **0.5.2 EPQ and Science Fair Project Ideas.** Knee themed research questions with method guidance.
- **0.5.3 Reading a Science Paper for the First Time.** A guided first read of a real paper. (Also deeper: 12.9)
- **0.5.4 Simple Biomechanics Experiments.** Safe home and classroom friendly experiments. (Also deeper: 3.1)
- **0.5.5 Meet the Researchers.** Profiles linking forward to the Research Academy. (Also deeper: 12.21; 12.24)

### Chapter 0.6 Junior Certificates and Challenges

Defaults for this chapter. Tiers: junior. Page type: assessment. Priority: low. Deeper spiral: 14.59. Chapter level must not cover: Diagnosis or treatment advice at any depth (Sections 4 to 8 own clinical content) | Commercial content of any kind (prohibited across Section 0).

- **0.6.1 Knee Explorer Certificate.** Gamified completion award for Chapters 0.1 and 0.2.
- **0.6.2 Future Surgeon Challenge.** Quiz ladder using the adaptive bank at beginner level. (Also deeper: 14.51)
- **0.6.3 School Leaderboards.** Class and school competitions, pre-moderated. (Also deeper: 14.79)
- **0.6.4 Digital Badges.** Shareable badges linked to progress tracking.

### Chapter 0.7 For Teachers, Coaches and Parents

Defaults for this chapter. Tiers: patient. Page type: teacher_resource. Priority: low. Deeper spiral: 10.62. Chapter level must not cover: Diagnosis or treatment advice at any depth (Sections 4 to 8 own clinical content) | Commercial content of any kind (prohibited across Section 0).

Note: Adult readers; written at Patient register. Section 0 governance still applies in full.

- **0.7.1 Ready-Made Lesson Plans.** Biology and PE lesson plans mapped to curricula.
- **0.7.2 Classroom Slide Decks and Worksheets.** Downloadable classroom assets.
- **0.7.3 Coaching Safely.** Load management and injury awareness for youth coaches. (Also deeper: 10.73; 11.42)
- **0.7.4 Supporting an Injured Young Athlete.** Parent guidance through injury and recovery. (Also deeper: 10.62; 10.69)
- **0.7.5 School Outreach Programme.** Talks, virtual theatre tours and careers events.

## Section 1: Knee Fundamentals


### Chapter 1.1 Introduction to the Knee

Defaults for this chapter. Tiers: junior, patient, medical_student. Page type: foundations. Priority: high. Deeper spiral: 2.1; 3.1. Chapter level must not cover: Structure level anatomy (owned by 1.2) | Individual condition detail (owned by Section 6).

- **1.1.1 What Is the Knee?.** The knee introduced as a joint and a working system.
- **1.1.2 Why the Knee Is Important.** Mobility, independence, sport and lifelong health.
- **1.1.3 Functions of the Knee.** Movement, load bearing and stability in outline. (Also must not cover: Kinematics detail (owned by 3.2 and 3.3). Also deeper: 3.1)
- **1.1.4 Evolution of the Human Knee.** Bipedalism and comparative anatomy in brief.
- **1.1.5 Common Knee Problems.** The major condition families named and oriented. (Also deeper: 6.141)
- **1.1.6 Lifelong Knee Health.** Everyday habits that protect the knee across life. (Also must not cover: Structured prevention programmes (owned by 11.21 to 11.27). Also deeper: 11.1)

### Chapter 1.2 Basic Knee Anatomy

Defaults for this chapter. Tiers: junior, patient, medical_student. Page type: anatomy. Priority: high. Deeper spiral: 2.1. Chapter level must not cover: Region level anatomy detail (owned per structure by Section 2) | Pathology (owned by Section 6) | Operative treatment (owned by Section 7).

- **1.2.1 Bones of the Knee.** Femur, tibia, fibula and patella oriented simply. (Also must not cover: Fracture patterns (owned by 6.96 to 6.101). Also deeper: 2.1; 2.2; 2.3; 2.4)
- **1.2.2 Articular Cartilage.** What cartilage is, does, and why it matters. (Also must not cover: Cartilage lesions (owned by 6.44 to 6.52) | Repair surgery (owned by 7.58 to 7.67). Also deeper: 3.5; 5.11; 6.44)
- **1.2.3 Menisci.** What the menisci are, where they sit, and why tears matter, in outline. (Also must not cover: Tear classification (owned by 6.28 to 6.33) | MRI grading (owned by 5.6.2) | Repair decisions (owned by 7.9) | Root anatomy detail (owned by 2.5.7 and 2.6.4). Also deeper: 2.5; 2.6; 3.6; 5.6; 6.27)
- **1.2.4 Ligaments.** The four main ligaments and their jobs. (Also must not cover: Bundle anatomy (owned by 2.7.8 and 2.7.9) | Reconstruction (owned by 7.20 onwards). Also deeper: 2.7; 2.8; 2.9; 2.10)
- **1.2.5 Tendons.** Quadriceps and patellar tendons introduced. (Also deeper: 4.16; 6.64)
- **1.2.6 Muscles Around the Knee.** The main muscle groups and their actions. (Also deeper: 11.9)
- **1.2.7 Nerves and Blood Supply.** Key vessels and nerves in outline. (Also must not cover: Surgical neurovascular anatomy (owned by 2.10.6 and Section 7). Also deeper: 2.10.6)
- **1.2.8 Synovium.** The joint lining and its fluid. (Also deeper: 5.14; 6.86)
- **1.2.9 Bursa.** The bursae around the knee and their role. (Also deeper: 5.5.2)
- **1.2.10 Growth Plates.** The physes introduced for young and adult readers. (Also must not cover: Physeal injuries (owned by 10.39 and 10.40). Also deeper: 10.2)

## Section 2: Anatomy Academy


### Chapter 2.1 Femur

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: anatomy. Priority: medium. Deeper spiral: 3.13; 5.3.2. Chapter level must not cover: Pathology of this structure (owned by 6.96 to 6.101) | Operative technique (owned by Section 7) | Imaging interpretation beyond normal anatomy (owned by Section 5) | Biomechanics beyond orientation (owned by 3.13).

- **2.1.1 Gross Anatomy.** Distal femoral osteology in overview.
- **2.1.2 Distal Femur.** Condylar geometry and bony landmarks.
- **2.1.3 Medial Femoral Condyle.** Shape, articular surface and landmarks.
- **2.1.4 Lateral Femoral Condyle.** Shape and its part in knee motion, oriented. (Also must not cover: Kinematic analysis (owned by 3.3))
- **2.1.5 Trochlea.** Trochlear geometry and its variation. (Also must not cover: Dysplasia classification (owned by 5.12.1 and 6.55). Also deeper: 2.12.1; 6.55)
- **2.1.6 Femoral Attachments of Ligaments.** Ligament attachment sites mapped on the femur. (Also deeper: 2.7.6; 2.9; 2.10)
- **2.1.7 Surgical Anatomy.** Approaches and at risk structures around the distal femur. (Tiers: medical_student, mrcs, frcs, fellowship)
- **2.1.8 Imaging Anatomy.** Radiological appearance of the distal femur. (Also deeper: 5.3; 5.5.2)
- **2.1.9 Biomechanical Relevance.** How femoral geometry shapes knee function. (Also deeper: 3.13)

### Chapter 2.2 Tibia

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: anatomy. Priority: medium. Deeper spiral: 3.13; 5.16. Chapter level must not cover: Pathology of this structure (owned by 6.96 to 6.101) | Operative technique (owned by Section 7) | Imaging interpretation beyond normal anatomy (owned by Section 5) | Biomechanics beyond orientation (owned by 3.13).

- **2.2.1 Proximal Tibia.** Proximal tibial osteology in overview.
- **2.2.2 Tibial Plateau.** Plateau geometry and posterior slope. (Also deeper: 6.96; 5.16.2)
- **2.2.3 Tibial Spine.** Intercondylar eminence and its attachments. (Also deeper: 6.101; 10.35)
- **2.2.4 Gerdy's Tubercle.** Landmark anatomy and iliotibial band attachment. (Also deeper: 2.11.1)
- **2.2.5 Tibial Tubercle.** Extensor attachment and its alignment relevance, oriented. (Also must not cover: Tubercle osteotomy technique (owned by 7.53) | TT-TG measurement method (owned by 5.16.4). Also deeper: 5.16.4; 7.53)
- **2.2.6 Surgical Anatomy.** Approaches and safe zones at the proximal tibia. (Tiers: medical_student, mrcs, frcs, fellowship)

### Chapter 2.3 Fibula

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: anatomy. Priority: low. Deeper spiral: 2.10. Chapter level must not cover: Pathology of this structure (owned by 6.26) | Operative technique (owned by 7.49) | Imaging interpretation beyond normal anatomy (owned by Section 5).

- **2.3.1 Anatomy.** Proximal fibular osteology.
- **2.3.2 Attachments.** LCL, biceps femoris and posterolateral attachments. (Also deeper: 2.10)
- **2.3.3 Clinical Importance.** Peroneal nerve proximity and surgical relevance. (Also deeper: 2.10.6; 7.49)

### Chapter 2.4 Patella

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: anatomy. Priority: medium. Deeper spiral: 3.12; 5.12. Chapter level must not cover: Pathology of this structure (owned by 6.53 to 6.63 and 6.97) | Operative technique (owned by 7.51 to 7.57) | Imaging interpretation beyond normal anatomy (owned by 5.12) | Biomechanics beyond orientation (owned by 3.12).

- **2.4.1 Anatomy.** Patellar osteology and facet anatomy.
- **2.4.2 Ossification.** Ossification pattern and bipartite variants. (Also deeper: 10.3.3)
- **2.4.3 Biomechanics.** Lever function of the patella, oriented. (Also deeper: 3.12)
- **2.4.4 Patellar Tracking.** Normal tracking anatomy through range. (Also deeper: 3.12.1; 4.15.1)
- **2.4.5 Surgical Relevance.** Relevance to instability surgery and arthroplasty. (Tiers: medical_student, mrcs, frcs, fellowship. Also deeper: 7.51; 7.79)

### Chapter 2.5 Medial Meniscus

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: anatomy. Priority: high. Deeper spiral: 3.6; 5.6; 6.27; 7.8. Chapter level must not cover: Pathology of this structure (owned by 6.27 to 6.43) | Operative technique (owned by 7.8 to 7.19) | Imaging interpretation beyond normal anatomy (owned by 5.6) | Biomechanics beyond orientation (owned by 3.6).

- **2.5.1 Gross Anatomy.** Shape, zones and attachments of the medial meniscus.
- **2.5.2 Histology.** Collagen architecture and cell biology.
- **2.5.3 Vascular Supply.** Red, red-white and white zones and healing relevance.
- **2.5.4 Biomechanics.** Load sharing role, oriented.
- **2.5.5 MRI Anatomy.** Normal appearance on MRI. (Also must not cover: Tear signal grading (owned by 5.6.2))
- **2.5.6 Surgical Anatomy.** Arthroscopic landmarks and access. (Tiers: medical_student, mrcs, frcs, fellowship)
- **2.5.7 Root Attachments.** Root anatomy and footprint landmarks. (Tiers: medical_student, mrcs, frcs, fellowship. Also deeper: 3.6.9; 6.34; 7.14)

### Chapter 2.6 Lateral Meniscus

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: anatomy. Priority: high. Deeper spiral: 3.6; 5.6; 6.27; 7.8. Chapter level must not cover: Pathology of this structure (owned by 6.27 to 6.43) | Operative technique (owned by 7.8 to 7.19) | Imaging interpretation beyond normal anatomy (owned by 5.6) | Biomechanics beyond orientation (owned by 3.6).

- **2.6.1 Gross Anatomy.** Shape, mobility and attachments of the lateral meniscus.
- **2.6.2 Popliteomeniscal Fascicles.** Fascicle anatomy and hypermobility relevance. (Tiers: medical_student, mrcs, frcs, fellowship)
- **2.6.3 Meniscofemoral Ligaments.** Humphrey and Wrisberg ligaments.
- **2.6.4 Root Attachments.** Root anatomy and footprint landmarks. (Tiers: medical_student, mrcs, frcs, fellowship. Also deeper: 3.6.9; 6.34; 7.14)
- **2.6.5 MRI Anatomy.** Normal appearance on MRI. (Also must not cover: Tear signal grading (owned by 5.6.2))
- **2.6.6 Surgical Anatomy.** Arthroscopic landmarks and access. (Tiers: medical_student, mrcs, frcs, fellowship)

### Chapter 2.7 ACL

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: anatomy. Priority: high. Deeper spiral: 3.7; 5.7; 6.1; 7.20. Chapter level must not cover: Pathology of this structure (owned by 6.1 to 6.8) | Operative technique (owned by 7.20 to 7.31) | Imaging interpretation beyond normal anatomy (owned by 5.7) | Biomechanics beyond orientation (owned by 3.7).

- **2.7.1 Gross Anatomy.** Dimensions, orientation and relations of the ACL.
- **2.7.2 Embryology.** Development of the ACL.
- **2.7.3 Histology.** Microstructure and insertional zones.
- **2.7.4 Blood Supply.** Middle genicular supply and healing relevance.
- **2.7.5 Innervation.** Nerve supply and mechanoreceptors.
- **2.7.6 Femoral Footprint.** Footprint morphology and bony landmarks. (Tiers: medical_student, mrcs, frcs, fellowship. Also must not cover: Tunnel drilling technique (owned by 7.20))
- **2.7.7 Tibial Footprint.** Tibial footprint morphology and landmarks. (Tiers: medical_student, mrcs, frcs, fellowship. Also must not cover: Tunnel drilling technique (owned by 7.20))
- **2.7.8 Anteromedial Bundle.** AM bundle anatomy. (Also must not cover: Bundle function through range (owned by 3.7.5))
- **2.7.9 Posterolateral Bundle.** PL bundle anatomy. (Also must not cover: Bundle function through range (owned by 3.7.6))
- **2.7.10 Proprioception.** Sensory role of the ACL. (Also deeper: 3.7; 8.10)
- **2.7.11 MRI Anatomy.** Normal ACL on MRI. (Also must not cover: Tear patterns (owned by 5.7.2 to 5.7.5))
- **2.7.12 Surgical Anatomy.** Arthroscopic landmarks for ACL surgery. (Tiers: medical_student, mrcs, frcs, fellowship)

### Chapter 2.8 PCL

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: anatomy. Priority: medium. Deeper spiral: 3.8; 5.8; 6.9; 7.32. Chapter level must not cover: Pathology of this structure (owned by 6.9 to 6.13) | Operative technique (owned by 7.32 to 7.37) | Imaging interpretation beyond normal anatomy (owned by 5.8) | Biomechanics beyond orientation (owned by 3.8).

- **2.8.1 Gross Anatomy.** Dimensions, orientation and relations of the PCL.
- **2.8.2 AL Bundle.** Anterolateral bundle anatomy.
- **2.8.3 PM Bundle.** Posteromedial bundle anatomy.
- **2.8.4 Blood Supply.** Vascular supply of the PCL.
- **2.8.5 MRI Anatomy.** Normal PCL on MRI. (Also must not cover: Tear patterns (owned by 5.8.2 and 5.8.3))
- **2.8.6 Surgical Anatomy.** Landmarks for PCL surgery. (Tiers: medical_student, mrcs, frcs, fellowship)

### Chapter 2.9 Medial Structures

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: anatomy. Priority: high. Deeper spiral: 3.9; 5.9; 6.14; 7.38. Chapter level must not cover: Pathology of this structure (owned by 6.14 to 6.20) | Operative technique (owned by 7.38 to 7.44) | Imaging interpretation beyond normal anatomy (owned by 5.9) | Biomechanics beyond orientation (owned by 3.9).

- **2.9.1 Superficial MCL.** Anatomy and attachments of the superficial MCL.
- **2.9.2 Deep MCL.** Meniscofemoral and meniscotibial portions.
- **2.9.3 Posterior Oblique Ligament.** POL anatomy and attachments.
- **2.9.4 Posteromedial Corner.** Layered anatomy of the posteromedial corner. (Tiers: medical_student, mrcs, frcs, fellowship)
- **2.9.5 Semimembranosus.** Insertional anatomy of semimembranosus.
- **2.9.6 Dynamic Stabilisation.** Dynamic medial stabilisers.
- **2.9.7 Surgical Anatomy.** Landmarks for medial knee surgery. (Tiers: medical_student, mrcs, frcs, fellowship)

### Chapter 2.10 Lateral Structures

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: anatomy. Priority: medium. Deeper spiral: 3.10; 5.10; 6.21; 7.45. Chapter level must not cover: Pathology of this structure (owned by 6.21 to 6.26) | Operative technique (owned by 7.45 to 7.50) | Imaging interpretation beyond normal anatomy (owned by 5.10) | Biomechanics beyond orientation (owned by 3.10).

- **2.10.1 LCL.** Anatomy and attachments of the LCL.
- **2.10.2 Popliteus Tendon.** Popliteus musculotendinous anatomy.
- **2.10.3 Popliteofibular Ligament.** PFL anatomy and attachments.
- **2.10.4 Posterolateral Corner.** Layered anatomy of the posterolateral corner. (Tiers: medical_student, mrcs, frcs, fellowship)
- **2.10.5 Biceps Femoris.** Insertional anatomy of biceps femoris.
- **2.10.6 Common Peroneal Nerve.** Course and surgical proximity of the nerve. (Also deeper: 6.26; 7.49)
- **2.10.7 Surgical Anatomy.** Landmarks for lateral and posterolateral surgery. (Tiers: medical_student, mrcs, frcs, fellowship)

### Chapter 2.11 Rotational Structures

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: anatomy. Priority: medium. Deeper spiral: 3.11; 7.30. Chapter level must not cover: Pathology of this structure (owned by 6.100) | Operative technique (owned by 7.30) | Imaging interpretation beyond normal anatomy (owned by 5.3.3) | Biomechanics beyond orientation (owned by 3.11).

- **2.11.1 Iliotibial Band.** ITB anatomy at the knee.
- **2.11.2 Kaplan Fibres.** Kaplan fibre anatomy and attachments. (Tiers: medical_student, mrcs, frcs, fellowship)
- **2.11.3 Anterolateral Ligament.** ALL anatomy and its identification. (Tiers: medical_student, mrcs, frcs, fellowship)
- **2.11.4 Segond Lesion.** Anatomy underlying the Segond fragment. (Also deeper: 6.100)
- **2.11.5 Anterolateral Complex.** The complex considered as a functional unit. (Tiers: medical_student, mrcs, frcs, fellowship. Also must not cover: Contemporary controversies (owned by 3.11.9))

### Chapter 2.12 Patellofemoral Anatomy

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: anatomy. Priority: high. Deeper spiral: 3.12; 5.12; 6.53; 7.51. Chapter level must not cover: Pathology of this structure (owned by 6.53 to 6.63) | Operative technique (owned by 7.51 to 7.57) | Imaging interpretation beyond normal anatomy (owned by 5.12) | Biomechanics beyond orientation (owned by 3.12).

- **2.12.1 Trochlea.** Trochlear anatomy for the patellofemoral joint. (Also deeper: 2.1.5)
- **2.12.2 MPFL.** MPFL anatomy and attachments.
- **2.12.3 MQTFL.** MQTFL anatomy and attachments. (Tiers: medical_student, mrcs, frcs, fellowship)
- **2.12.4 Retinacula.** Medial and lateral retinacular anatomy.
- **2.12.5 Dynamic Stabilisers.** Dynamic stabilisers of the patella.
- **2.12.6 Surgical Anatomy.** Landmarks for patellofemoral surgery. (Tiers: medical_student, mrcs, frcs, fellowship)

## Section 3: Biomechanics Academy


### Chapter 3.1 Introduction to Knee Biomechanics

Defaults for this chapter. Tiers: junior, patient, medical_student, mrcs. Page type: biomechanics. Priority: medium. Deeper spiral: 3.2. Chapter level must not cover: Examination technique (owned by Section 4) | Imaging interpretation (owned by Section 5) | Clinical management (owned by Section 6) | Operative technique (owned by Section 7).

- **3.1.1 What Is Biomechanics?.** The discipline defined for every learner.
- **3.1.2 Why Biomechanics Matters.** From forces to injury and treatment, the link explained.
- **3.1.3 Biomechanics in Everyday Life.** Stairs, squatting and walking as worked examples.
- **3.1.4 Biomechanics in Sport.** Sporting demands on the knee in outline. (Also deeper: 3.15)
- **3.1.5 Biomechanics and Injury Prevention.** The idea of modifiable mechanics. (Also deeper: 11.21)
- **3.1.6 Biomechanics and Surgical Reconstruction.** Why surgeons study mechanics. (Tiers: medical_student, mrcs, frcs. Also deeper: 3.7.20)
- **3.1.7 Historical Development of Knee Biomechanics.** How the field developed. (Tiers: frcs, fellowship, consultant)
- **3.1.8 Landmark Biomechanical Studies.** Orientation to the classic studies. (Tiers: frcs, fellowship, consultant. Type: landmark_papers. Also must not cover: Per topic landmark detail (owned by 3.17))

### Chapter 3.2 Functional Anatomy and Motion

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: biomechanics. Priority: medium. Deeper spiral: 3.3. Chapter level must not cover: Examination technique (owned by Section 4) | Imaging interpretation (owned by Section 5) | Clinical management (owned by Section 6) | Operative technique (owned by Section 7) | Per ligament restraint function (owned by 3.7 to 3.11).

- **3.2.1 Degrees of Freedom of the Knee.** The six degrees of freedom introduced.
- **3.2.2 Flexion and Extension.** Sagittal motion and its normal range.
- **3.2.3 Internal Rotation.** Internal rotation and its restraints, oriented.
- **3.2.4 External Rotation.** External rotation and its restraints, oriented.
- **3.2.5 Varus Motion.** Varus angulation and its restraints, oriented.
- **3.2.6 Valgus Motion.** Valgus angulation and its restraints, oriented.
- **3.2.7 Anterior Translation.** Anterior tibial translation, oriented. (Also must not cover: Lachman correlation (owned by 4.10.4))
- **3.2.8 Posterior Translation.** Posterior tibial translation, oriented.
- **3.2.9 Coupled Motion.** How motions couple during function.
- **3.2.10 Knee Stability During Motion.** Synthesis of stability through range.

### Chapter 3.3 Knee Kinematics

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: biomechanics. Priority: medium. Deeper spiral: 3.14. Chapter level must not cover: Examination technique (owned by Section 4) | Imaging interpretation (owned by Section 5) | Clinical management (owned by Section 6) | Operative technique (owned by Section 7) | Gait pathology (owned by 3.14 and 4.4) | Sport specific application (owned by 3.15).

- **3.3.1 Introduction to Kinematics.** How knee motion is described and measured.
- **3.3.2 Roll and Glide Mechanisms.** The femorotibial roll and glide relationship.
- **3.3.3 Femoral Motion on Tibia.** Closed chain motion described.
- **3.3.4 Tibial Motion on Femur.** Open chain motion described.
- **3.3.5 Screw Home Mechanism.** Terminal extension rotation explained.
- **3.3.6 Reverse Screw Home Mechanism.** Unlocking from full extension.
- **3.3.7 Instant Centre of Rotation.** The moving axis of the knee.
- **3.3.8 Changes Throughout Flexion.** How kinematics change through range.
- **3.3.9 Kinematics During Walking.** Knee motion in gait.
- **3.3.10 Kinematics During Running.** Knee motion in running.
- **3.3.11 Kinematics During Squatting.** Knee motion in squatting.
- **3.3.12 Kinematics During Stair Climbing.** Knee motion on stairs.
- **3.3.13 Kinematics During Landing.** Knee motion in landing. (Also deeper: 3.7.12; 11.7)
- **3.3.14 Kinematics During Cutting.** Knee motion in cutting. (Also deeper: 3.7.13; 11.19)

### Chapter 3.4 Knee Kinetics

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: biomechanics. Priority: medium. Deeper spiral: 3.5. Chapter level must not cover: Examination technique (owned by Section 4) | Imaging interpretation (owned by Section 5) | Clinical management (owned by Section 6) | Operative technique (owned by Section 7).

- **3.4.1 Introduction to Kinetics.** Forces and moments at the knee defined.
- **3.4.2 Ground Reaction Forces.** Magnitude and direction across activities.
- **3.4.3 Joint Reaction Forces.** Tibiofemoral and patellofemoral joint loads.
- **3.4.4 Lever Arms.** Moment arms about the knee.
- **3.4.5 Moments About the Knee.** Net moment concepts.
- **3.4.6 External Moments.** Externally applied moments during activity.
- **3.4.7 Internal Moments.** Muscle and ligament counter moments.
- **3.4.8 Energy Absorption.** Eccentric energy absorption at the knee.
- **3.4.9 Force Transmission.** Load paths through the joint.
- **3.4.10 Shock Absorption.** Structures damping impact load. (Also must not cover: Meniscal shock absorption detail (owned by 3.6.6))

### Chapter 3.5 Tibiofemoral Contact Mechanics

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: biomechanics. Priority: medium. Deeper spiral: 3.6; 3.13. Chapter level must not cover: Examination technique (owned by Section 4) | Imaging interpretation (owned by Section 5) | Clinical management (owned by Section 6) | Operative technique (owned by Section 7).

- **3.5.1 Contact Areas.** Normal tibiofemoral contact areas.
- **3.5.2 Contact Pressures.** Normal contact pressure magnitudes.
- **3.5.3 Load Distribution.** Medial to lateral load share.
- **3.5.4 Effects of Flexion.** Contact change through range.
- **3.5.5 Effects of Meniscal Loss.** Pressure rise after meniscal loss. (Also deeper: 6.37; 7.8)
- **3.5.6 Effects of Malalignment.** Varus and valgus compartment overload. (Also deeper: 3.13; 7.68)
- **3.5.7 Effects of Obesity.** Load scaling with body mass. (Also deeper: 6.78)
- **3.5.8 Contact Mechanics After ACL Injury.** Altered contact after ACL injury. (Also deeper: 6.5)
- **3.5.9 Contact Mechanics After Meniscectomy.** Altered contact after partial meniscectomy. (Also deeper: 7.8)
- **3.5.10 Contact Mechanics After Osteotomy.** Unloading effect of realignment. (Also deeper: 7.69)

### Chapter 3.6 Meniscal Biomechanics

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: biomechanics. Priority: high. Deeper spiral: 6.27; 7.8. Chapter level must not cover: Examination technique (owned by Section 4) | Imaging interpretation (owned by Section 5) | Clinical management (owned by Section 6) | Operative technique (owned by Section 7) | Tear classification (owned by 6.28 to 6.43) | MRI appearances (owned by 5.6).

- **3.6.1 Functions of the Meniscus.** The functional roles of the menisci summarised.
- **3.6.2 Hoop Stress.** The circumferential stress principle.
- **3.6.3 Circumferential Fibres.** Fibre architecture carrying hoop stress.
- **3.6.4 Radial Fibres.** Tie fibres resisting longitudinal splitting.
- **3.6.5 Load Sharing.** The proportion of joint load carried.
- **3.6.6 Shock Absorption.** The damping role of the menisci.
- **3.6.7 Joint Lubrication.** Contribution to joint lubrication.
- **3.6.8 Proprioception.** The sensory role of the menisci.
- **3.6.9 Root Biomechanics.** Root integrity and hoop function. (Also deeper: 6.34; 7.14)
- **3.6.10 Meniscal Extrusion.** Mechanics of meniscal extrusion. (Also deeper: 5.6.11; 6.36)
- **3.6.11 Effects of Root Tears.** The functional meniscectomy concept. (Also deeper: 6.34)
- **3.6.12 Effects of Radial Tears.** Hoop disruption by radial tears. (Also deeper: 6.31)
- **3.6.13 Meniscal Repair Biomechanics.** Fixation construct behaviour. (Tiers: medical_student, mrcs, frcs, fellowship. Also deeper: 7.9)
- **3.6.14 Meniscal Transplantation Biomechanics.** Allograft function and fixation. (Tiers: medical_student, mrcs, frcs, fellowship. Also deeper: 7.18)

### Chapter 3.7 ACL Biomechanics

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: biomechanics. Priority: high. Deeper spiral: 6.1; 7.20. Chapter level must not cover: Examination technique (owned by Section 4) | Imaging interpretation (owned by Section 5) | Clinical management (owned by Section 6) | Operative technique (owned by Section 7) | Reconstruction technique (owned by 7.20 to 7.31) | Examination tests (owned by 4.10).

- **3.7.1 Functions of the ACL.** The functional roles of the ACL summarised.
- **3.7.2 Primary Restraints.** The ACL as primary restraint to anterior translation.
- **3.7.3 Secondary Restraints.** Secondary restraint interplay.
- **3.7.4 Bundle Function.** The two bundle model in overview.
- **3.7.5 AM Bundle Function.** Anteromedial bundle function through range.
- **3.7.6 PL Bundle Function.** Posterolateral bundle function through range.
- **3.7.7 Rotational Stability.** The ACL role in rotational control.
- **3.7.8 Anterior Stability.** The ACL role in anterior stability.
- **3.7.9 Pivot Shift Mechanics.** Subluxation and reduction mechanics. (Also deeper: 4.10.6)
- **3.7.10 ACL Strain During Activity.** Strain behaviour across common activities.
- **3.7.11 ACL Loading During Running.** Loading during running.
- **3.7.12 ACL Loading During Landing.** Loading during landing. (Also deeper: 11.7)
- **3.7.13 ACL Loading During Cutting.** Loading during cutting. (Also deeper: 11.19)
- **3.7.14 ACL Injury Mechanisms.** Mechanism synthesis from video and laboratory data. (Also deeper: 6.1.5; 11.21)
- **3.7.15 Female ACL Biomechanics.** Sex specific mechanics and risk. (Also deeper: 9.3; 9.10)
- **3.7.16 Graft Biomechanics.** Graft material properties compared. (Tiers: medical_student, mrcs, frcs, fellowship)
- **3.7.17 Hamstring Graft Biomechanics.** Hamstring graft behaviour. (Tiers: medical_student, mrcs, frcs, fellowship. Also deeper: 7.21)
- **3.7.18 Patellar Tendon Graft Biomechanics.** Patellar tendon graft behaviour. (Tiers: medical_student, mrcs, frcs, fellowship. Also deeper: 7.22)
- **3.7.19 Quadriceps Tendon Graft Biomechanics.** Quadriceps graft behaviour. (Tiers: medical_student, mrcs, frcs, fellowship. Also deeper: 7.23)
- **3.7.20 ACL Reconstruction Biomechanics.** Construct behaviour after reconstruction. (Tiers: medical_student, mrcs, frcs, fellowship. Also deeper: 7.20)

### Chapter 3.8 PCL Biomechanics

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: biomechanics. Priority: medium. Deeper spiral: 6.9; 7.32. Chapter level must not cover: Examination technique (owned by Section 4) | Imaging interpretation (owned by Section 5) | Clinical management (owned by Section 6) | Operative technique (owned by Section 7).

- **3.8.1 Functions of the PCL.** The functional roles of the PCL summarised.
- **3.8.2 Posterior Stability.** The PCL as primary posterior restraint.
- **3.8.3 Bundle Function.** The two bundle model of the PCL.
- **3.8.4 AL Bundle Mechanics.** Anterolateral bundle mechanics.
- **3.8.5 PM Bundle Mechanics.** Posteromedial bundle mechanics.
- **3.8.6 Posterior Drawer Mechanics.** Mechanics behind the posterior drawer. (Also deeper: 4.11.2)
- **3.8.7 Gait Following PCL Injury.** Gait adaptation after PCL injury. (Also deeper: 3.14.10; 4.4.4)
- **3.8.8 PCL Reconstruction Biomechanics.** Reconstruction construct behaviour. (Tiers: medical_student, mrcs, frcs, fellowship. Also deeper: 7.32)
- **3.8.9 Double Bundle Reconstruction.** Double bundle rationale and mechanics. (Tiers: medical_student, mrcs, frcs, fellowship. Also deeper: 7.34)
- **3.8.10 Inlay Techniques.** Tibial inlay mechanics. (Tiers: medical_student, mrcs, frcs, fellowship. Also deeper: 7.35)

### Chapter 3.9 Medial Knee Biomechanics

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: biomechanics. Priority: medium. Deeper spiral: 6.14; 7.38. Chapter level must not cover: Examination technique (owned by Section 4) | Imaging interpretation (owned by Section 5) | Clinical management (owned by Section 6) | Operative technique (owned by Section 7).

- **3.9.1 Valgus Stability.** Restraints to valgus load.
- **3.9.2 Rotational Stability.** Medial contribution to rotational control.
- **3.9.3 Superficial MCL Function.** Superficial MCL function through range.
- **3.9.4 Deep MCL Function.** Deep MCL function through range.
- **3.9.5 POL Function.** POL function through range.
- **3.9.6 Posteromedial Corner Function.** The corner as a functional unit.
- **3.9.7 AMRI Biomechanics.** Anteromedial rotatory instability mechanics. (Also deeper: 4.12.6; 6.18; 7.43)
- **3.9.8 Medial Reconstruction Biomechanics.** Medial reconstruction construct behaviour. (Tiers: medical_student, mrcs, frcs, fellowship. Also deeper: 7.38)
- **3.9.9 Contributions at Different Flexion Angles.** Restraint share across flexion.
- **3.9.10 Combined ACL and MCL Injury.** Combined injury mechanics. (Also deeper: 6.20; 7.44)

### Chapter 3.10 Lateral Knee Biomechanics

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: biomechanics. Priority: medium. Deeper spiral: 6.21; 7.45. Chapter level must not cover: Examination technique (owned by Section 4) | Imaging interpretation (owned by Section 5) | Clinical management (owned by Section 6) | Operative technique (owned by Section 7).

- **3.10.1 Varus Stability.** Restraints to varus load.
- **3.10.2 External Rotation Stability.** Restraints to external rotation.
- **3.10.3 LCL Function.** LCL function through range.
- **3.10.4 Popliteus Function.** Popliteus function through range.
- **3.10.5 Popliteofibular Ligament Function.** PFL function through range.
- **3.10.6 Posterolateral Corner Function.** The corner as a functional unit.
- **3.10.7 Dial Test Biomechanics.** Mechanics behind the dial test. (Also deeper: 4.13.5)
- **3.10.8 PLC Reconstruction Biomechanics.** PLC reconstruction construct behaviour. (Tiers: medical_student, mrcs, frcs, fellowship. Also deeper: 7.46)
- **3.10.9 Combined PCL and PLC Injury.** Combined injury mechanics. (Also deeper: 6.24; 7.48)

### Chapter 3.11 Anterolateral Complex Biomechanics

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: biomechanics. Priority: medium. Deeper spiral: 6.100; 7.30. Chapter level must not cover: Examination technique (owned by Section 4) | Imaging interpretation (owned by Section 5) | Clinical management (owned by Section 6) | Operative technique (owned by Section 7).

- **3.11.1 Iliotibial Band Function.** ITB function at the knee.
- **3.11.2 Kaplan Fibre Function.** Kaplan fibre restraint role. (Tiers: medical_student, mrcs, frcs, fellowship)
- **3.11.3 Anterolateral Ligament Function.** ALL restraint role. (Tiers: medical_student, mrcs, frcs, fellowship)
- **3.11.4 Pivot Shift Control.** Anterolateral control of the pivot shift.
- **3.11.5 Internal Rotation Control.** Restraint of internal rotation.
- **3.11.6 Segond Lesion Mechanics.** Mechanics producing the Segond fragment. (Also deeper: 6.100)
- **3.11.7 Lateral Extra-articular Tenodesis.** Tenodesis mechanics and effect. (Tiers: medical_student, mrcs, frcs, fellowship. Also deeper: 7.30)
- **3.11.8 Combined ACL and ALL Reconstruction.** Combined reconstruction mechanics. (Tiers: medical_student, mrcs, frcs, fellowship. Also deeper: 7.30)
- **3.11.9 Contemporary Controversies.** The anterolateral debate stated fairly. (Tiers: frcs, fellowship, consultant)

### Chapter 3.12 Patellofemoral Biomechanics

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: biomechanics. Priority: medium. Deeper spiral: 6.53; 7.51. Chapter level must not cover: Examination technique (owned by Section 4) | Imaging interpretation (owned by Section 5) | Clinical management (owned by Section 6) | Operative technique (owned by Section 7).

- **3.12.1 Patellar Tracking.** Normal tracking mechanics.
- **3.12.2 Contact Areas.** Patellofemoral contact areas through range.
- **3.12.3 Contact Pressures.** Patellofemoral pressure magnitudes.
- **3.12.4 Trochlear Function.** Trochlear constraint of the patella.
- **3.12.5 MPFL Function.** MPFL restraint role.
- **3.12.6 Q Angle.** The Q angle and its limitations.
- **3.12.7 Dynamic Valgus.** Dynamic valgus and patellar load. (Also deeper: 9.3.1; 11.7.2)
- **3.12.8 Patellar Instability.** Mechanics of patellar instability. (Also deeper: 6.54)
- **3.12.9 Patellofemoral Pain.** Mechanical contributors to patellofemoral pain. (Also deeper: 6.60)
- **3.12.10 Patellofemoral Arthritis.** Mechanics of patellofemoral wear. (Also deeper: 6.62)
- **3.12.11 Effects of Malalignment.** Alignment effects on the patellofemoral joint.
- **3.12.12 Tibial Tubercle Position.** Tubercle position and patellar mechanics. (Also deeper: 5.16.4; 7.53)

### Chapter 3.13 Alignment and Biomechanics

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: biomechanics. Priority: medium. Deeper spiral: 5.3.2; 7.68. Chapter level must not cover: Examination technique (owned by Section 4) | Imaging interpretation (owned by Section 5) | Clinical management (owned by Section 6) | Operative technique (owned by Section 7).

- **3.13.1 Mechanical Axis.** The mechanical axis defined.
- **3.13.2 Anatomical Axis.** The anatomical axis defined.
- **3.13.3 Varus Alignment.** Varus alignment and its load effects.
- **3.13.4 Valgus Alignment.** Valgus alignment and its load effects.
- **3.13.5 Constitutional Varus.** Constitutional varus and its relevance.
- **3.13.6 Joint Line Obliquity.** Joint line obliquity and its limits.
- **3.13.7 Dynamic Alignment.** Alignment under dynamic load.
- **3.13.8 Alignment and OA.** Alignment as a driver of osteoarthritis. (Also deeper: 6.71)
- **3.13.9 Osteotomy Biomechanics.** Mechanics of realignment osteotomy. (Tiers: medical_student, mrcs, frcs, fellowship. Also deeper: 7.68)
- **3.13.10 Alignment Correction Principles.** Correction targets and their rationale. (Tiers: medical_student, mrcs, frcs, fellowship. Also deeper: 7.68)

### Chapter 3.14 Gait Analysis

Defaults for this chapter. Tiers: medical_student, mrcs, frcs. Page type: biomechanics. Priority: medium. Deeper spiral: 4.4. Chapter level must not cover: Examination technique (owned by Section 4) | Imaging interpretation (owned by Section 5) | Clinical management (owned by Section 6) | Operative technique (owned by Section 7) | Gait examination technique (owned by 4.4).

- **3.14.1 Normal Gait.** The normal gait cycle at the knee. (Tiers: medical_student, mrcs, frcs, patient)
- **3.14.2 Stance Phase.** Knee mechanics in stance.
- **3.14.3 Swing Phase.** Knee mechanics in swing.
- **3.14.4 Running Gait.** Knee mechanics in running.
- **3.14.5 Sprinting.** Knee mechanics in sprinting.
- **3.14.6 Cutting Manoeuvres.** Knee mechanics in cutting.
- **3.14.7 Jumping.** Knee mechanics in jumping.
- **3.14.8 Landing.** Knee mechanics in landing.
- **3.14.9 ACL Deficient Gait.** Gait adaptation in ACL deficiency. (Also deeper: 6.5)
- **3.14.10 PCL Deficient Gait.** Gait adaptation in PCL deficiency. (Also deeper: 6.10)
- **3.14.11 Arthritic Gait.** Gait adaptation in osteoarthritis. (Also deeper: 6.80)
- **3.14.12 Post-Arthroplasty Gait.** Gait after knee replacement. (Also deeper: 8.45)

### Chapter 3.15 Sports-Specific Knee Biomechanics

Defaults for this chapter. Tiers: patient, medical_student, mrcs. Page type: biomechanics. Priority: medium. Deeper spiral: 11.28. Chapter level must not cover: Examination technique (owned by Section 4) | Imaging interpretation (owned by Section 5) | Clinical management (owned by Section 6) | Operative technique (owned by Section 7) | Sport performance training (owned by 11 Part H).

- **3.15.1 Football.** Knee demands and injury mechanics in football. (Also deeper: 11.28)
- **3.15.2 Cricket.** Knee demands and injury mechanics in cricket. (Also deeper: 11.29)
- **3.15.3 Rugby.** Knee demands and injury mechanics in rugby. (Also deeper: 11.30)
- **3.15.4 Tennis.** Knee demands and injury mechanics in tennis. (Also deeper: 11.31)
- **3.15.5 Basketball.** Knee demands and injury mechanics in basketball. (Also deeper: 11.32)
- **3.15.6 Skiing.** Knee demands and injury mechanics in skiing. (Also deeper: 11.35)
- **3.15.7 Athletics.** Knee demands and injury mechanics in athletics. (Also deeper: 11.33)
- **3.15.8 Cycling.** Knee demands and injury mechanics in cycling.
- **3.15.9 Golf.** Knee demands and injury mechanics in golf. (Also deeper: 11.34)
- **3.15.10 Dance.** Knee demands and injury mechanics in dance.

### Chapter 3.16 Advanced Biomechanics

Defaults for this chapter. Tiers: frcs, fellowship, consultant. Page type: biomechanics. Priority: low. Deeper spiral: 12.18. Chapter level must not cover: Examination technique (owned by Section 4) | Imaging interpretation (owned by Section 5) | Clinical management (owned by Section 6) | Operative technique (owned by Section 7).

- **3.16.1 Cadaveric Testing.** Cadaveric testing methods and limits. (Also deeper: 12.18.1)
- **3.16.2 Robotic Testing Systems.** Robotic testing methods. (Also deeper: 12.18.3)
- **3.16.3 Navigation Systems.** Navigation as a measurement tool.
- **3.16.4 Finite Element Modelling.** Finite element methods for the knee. (Also deeper: 12.20)
- **3.16.5 Computational Biomechanics.** Computational modelling approaches.
- **3.16.6 Artificial Intelligence.** Machine learning in biomechanics. (Also deeper: 12.49)
- **3.16.7 Motion Capture.** Motion capture methods. (Also deeper: 8.78; 11.58)
- **3.16.8 Wearable Technology.** Wearable measurement of knee load. (Also deeper: 11.56)
- **3.16.9 Digital Twins.** Digital twin concepts for the knee. (Also deeper: 12.53)
- **3.16.10 Future Directions.** Where measurement is heading.

### Chapter 3.17 Landmark Biomechanics Papers

Defaults for this chapter. Tiers: frcs, fellowship, consultant. Page type: landmark_papers. Priority: low. Deeper spiral: 12.33. Chapter level must not cover: Topic teaching content (owned by the matching 3.x chapter).

- **3.17.1 ACL Landmark Studies.** Curated landmark ACL biomechanics studies with appraisal notes.
- **3.17.2 PCL Landmark Studies.** Curated landmark PCL biomechanics studies with appraisal notes.
- **3.17.3 Meniscal Landmark Studies.** Curated landmark meniscal studies with appraisal notes.
- **3.17.4 Medial Knee Landmark Studies.** Curated landmark medial knee studies with appraisal notes.
- **3.17.5 PLC Landmark Studies.** Curated landmark posterolateral studies with appraisal notes.
- **3.17.6 Patellofemoral Landmark Studies.** Curated landmark patellofemoral studies with appraisal notes.
- **3.17.7 Osteotomy Landmark Studies.** Curated landmark osteotomy studies with appraisal notes.
- **3.17.8 Arthroplasty Landmark Studies.** Curated landmark arthroplasty studies with appraisal notes.
- **3.17.9 Imperial Knee Biomechanics Contributions.** The platform's own research programme summarised; consultant review of claims mandatory. (Also deeper: 12.21)
- **3.17.10 Future Research Priorities.** Open questions the field should answer next.


---

## Instalment Plan

This is Part 1 of 6. Ask for the next instalment by name; each arrives in this exact format with its JSON seed:

- Part 2: Sections 4 and 5 (examination and imaging, roughly 400 to 550 pages)
- Part 3: Section 6 (conditions, roughly 500 to 700 pages, likely split A to J and K to T)
- Part 4: Section 7 (surgery, roughly 450 to 600 pages)
- Part 5: Sections 8 to 11 (rehabilitation, women's, children's, performance)
- Part 6: Sections 12 to 15 (research, cases, questions, video)

## Open Questions

1. **Tier assignments are editorial defaults.** In particular: Section 2 carries no Patient tier (Section 1 owns patient level anatomy), Section 3's introduction carries Junior and Patient, and surgical anatomy pages add Fellowship. Editor in Chief to sign off before batch runs.
2. **Chapter 0.7 serves adults.** Its pages are written at Patient register inside Section 0; Section 0 governance, including the commercial ban, still applies in full. Confirm this treatment.
3. **Single page chapters.** From Section 6 onwards, chapters without numbered sub pages are treated as one page each unless their instalment splits them. Confirm before Part 3.
4. **KneeSchool_Table_of_Contents.pdf uses a different numbering** (sections running to 23). It conflicts with this architecture and should be retired or regenerated from it, to avoid a third structure in circulation.
5. **Deeper links into Sections 4 to 15** reference chapters that exist in the source skeleton but whose page level splits are not yet fixed. Chapter level ids are stable; page level ids in those sections are provisional until their instalment lands.
6. **Word counts and page types** for the variant types in Section 6 of this document need Handbook v1.1 rulings (Handbook Open Question 5).
7. **3.17.9 and other internal programme pages** (Imperial contributions, Sportshealing and OmKneeHealth titled chapters) describe the platform owner's own work and products; consultant review must confirm claims, and the commercial pages must respect the tier governance rules, in particular the Junior ban.
