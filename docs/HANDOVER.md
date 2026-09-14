# KneeSchool.com Build Handover

Version 1.0. Prepared for continuation in Claude Code.

---

## 1. Read this first

You are continuing a static front end build for **KneeSchool.com**, an educational platform about knee health.

Current state: one finished homepage, `kneeschool.html`, self contained HTML and CSS, no JavaScript, no build step.

Your job is to extend it into a multi page static site without breaking the visual system or the copy rules below.

---

## 2. Product summary

| Item | Detail |
|---|---|
| Site | KneeSchool.com |
| Audience | Knee pain sufferers aged 11 to 99, all backgrounds, plus medical students, surgical trainees, fellows and consultants |
| Core idea | A spiral syllabus. The same topic is taught repeatedly at increasing depth |
| Levels | Patient, Student (A level to MBBS), MRCS, FRCS (Tr and Orth), Fellowship, Consultant Masterclass |
| Tone | Academic authority, plain speech, British English |
| Commercial links | Sportshealing clinical services, OmKneeHealth products, both currently unlinked placeholders |

Source documents sit in the project knowledge:

- `KneeSchool_Master_Playbook_v1.docx`
- `KneeSchool_Sections_1_to_15_Full_Architecture.docx`
- `KneeSchool_Master_Playbook.pdf`
- `KneeSchool_Table_of_Contents.pdf`
- `KneeSchool_Operations_Handbook.pdf`
- `KneeSchool_Master_Operations_Handbook.pdf`

Read the Operations Handbook before writing any clinical copy. It contains the article template, editorial standards and the approved prompt library.

---

## 3. What already exists

File: `kneeschool.html`

Sections in document order:

1. **Header.** Wordmark, six item nav, checkbox driven mobile menu at 860px and below.
2. **Hero.** Headline, sub copy, two buttons, plus the depth dial.
3. **Depth dial.** The signature component. One topic, the ACL, written six ways. Six radio inputs, six labels, six panels. Pure CSS, no script.
4. **How the spiral works.** Three numbered steps. Numbers are used because the content is a real sequence.
5. **Learn by level.** Six row ladder. Each row has name, audience, one line summary, a link, and a six segment depth bar showing position in the curriculum.
6. **Knee encyclopaedia.** Four columns: Structure, Function, Assessment, Treatment.
7. **Conditions library.** Twelve item multi column list.
8. **Whole body panel.** Six factors outside the joint that drive knee pain.
9. **Practise, test, track.** Four tools: question bank, case library, video academy, knee score centre.
10. **Closing call to action.**
11. **Footer.** Four link groups, safety notice with red flags, copyright.

All internal links currently point to `#`. Nav links point to on page anchors.

---

## 4. Design system

### Colour tokens

Declared in `:root`. Do not introduce new colours without replacing an existing token.

```css
--green-900:#0E2A21;   /* page dark, header, hero, footer */
--green-800:#123428;   /* second dark band, dial panel */
--green-700:#174336;   /* call to action band */
--green-500:#2E6B56;   /* depth bar fill on light */
--ivory:#F5F1E6;       /* page light */
--ivory-2:#EAE3D2;     /* empty depth segment on light */
--ink:#16221D;         /* body text on ivory */
--ink-soft:#41504A;    /* secondary text on ivory */
--gold:#C3A046;        /* accent, active states, buttons */
--gold-dark:#8F701F;   /* gold that passes contrast on ivory */
```

Rule: gold never carries body text on ivory. Use `--gold-dark` for that case.

### Type

```css
--display:"Newsreader", "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
--body:"Source Serif 4", "Iowan Old Style", Georgia, "Times New Roman", serif;
```

- Fonts load from Google Fonts. The fallback stack is deliberate so Windows, macOS and iOS all render a serif if the request fails.
- Headings use weight 300 or 400 only. No bold headings.
- Body is `clamp(1.02rem, .96rem + .35vw, 1.15rem)` at line height 1.68.
- Line length capped near 66 characters by `--measure`.

### Layout

- `.wrap` sets max width 76rem and the horizontal gutter from `--pad`.
- `.band` sets vertical section rhythm.
- `.dark` flips a band to green with ivory text.
- Dark and light bands alternate. Two dark bands in a row are separated by `--green-800`.
- Breakpoints in use: 900, 860, 820, 760, 620, 560.

### Quality floor, already met, keep it met

- Visible keyboard focus through `:focus-visible`.
- `prefers-reduced-motion` disables transitions and smooth scroll.
- No `localStorage` or `sessionStorage`.
- Tag structure validated, zero unclosed elements.
- No em dashes or en dashes anywhere in the file.

---

## 5. Copy rules, non negotiable

1. British English. Encyclopaedia, paediatric, randomised.
2. No em dashes and no en dashes. Use full stops or commas.
3. Short sentences. One idea each. No chained reasoning.
4. No repetition across sections.
5. Sentence case for headings and buttons. No all caps labels.
6. Buttons name the action. "Score your knee", not "Submit".
7. No unsupported clinical claims. No invented references.
8. Every clinical page carries the educational disclaimer and red flag advice already used in the footer.

---

## 6. Next tasks, in order

### Task 1. Split into a site skeleton

Create `/index.html` from the current file, then add:

```
/index.html
/levels/patient.html
/levels/student.html
/levels/mrcs.html
/levels/frcs.html
/levels/fellowship.html
/levels/consultant.html
/conditions/acl.html          (template article)
/assets/styles.css            (extract the current inline CSS)
```

Keep one shared stylesheet once more than one page exists. Do not duplicate CSS per page.

### Task 2. Build the level landing template

Each level page needs:

- Level name, audience line, depth bar showing position.
- What you will cover, as a short list.
- Entry test or starting topic.
- The topic grid for that level.
- Link up and down to the adjacent levels.

### Task 3. Build the condition article template

Follow the Operations Handbook article template:

Overview, Patient section, Student section, MRCS section, FRCS section, Fellowship section, key learning points, imaging, treatment, rehabilitation, controversies, references.

Reuse the depth dial pattern for the level sections so the article shows one topic at six depths. This is the site's core mechanic and should appear on every condition page.

### Task 4. Search

The playbook asks for a search first homepage. Current homepage leads with the depth dial instead. Decide with the client before building. If search is added, a static site needs either a prebuilt JSON index or a hosted search service.

### Task 5. Progress tracking

Deferred. It needs accounts and a backend. Do not fake it with browser storage.

---

## 7. Known gaps

- Brand assets from chinmaygupte.com are not confirmed. Colours were matched by eye against the stated deep green, ivory and gold identity. Request the logo SVG and official hex values.
- No images. The interactive knee model, MRI sliders and video library are all specified in the playbook and all absent.
- Sportshealing and OmKneeHealth appear as generic footer links, not named.
- All clinical copy on the homepage is illustrative. It must pass consultant review before publication.
- No analytics, schema markup or meta tags beyond title, description and theme colour.

---

## 8. How to verify a change

```bash
# structural check
python3 - <<'EOF'
from html.parser import HTMLParser
VOID={'area','base','br','col','embed','hr','img','input','link','meta','source','track','wbr'}
class P(HTMLParser):
    def __init__(s): super().__init__(); s.st=[]; s.err=[]
    def handle_starttag(s,t,a):
        if t not in VOID: s.st.append(t)
    def handle_endtag(s,t):
        if not s.st or s.st[-1]!=t: s.err.append((t,s.getpos()))
        else: s.st.pop()
p=P(); txt=open('index.html').read(); p.feed(txt)
print("errors:",p.err,"unclosed:",p.st)
print("dashes:", '\u2014' in txt or '\u2013' in txt)
EOF
```

Then check by eye at 375px, 768px and 1440px widths.

Note: `wkhtmltoimage` is available in the container but runs an old WebKit engine that ignores CSS grid and blocks web fonts. Its screenshots are not a reliable preview. Use it only for gross layout checks.

---

## Questions

1. Do you want the site split into the multi page skeleton in section 6, or kept as single page for now?
2. Can you supply the chinmaygupte.com logo and exact brand hex values?
3. Which condition should be built first as the article template, ACL or osteoarthritis?
4. Is the homepage to lead with search, as the playbook states, or with the depth dial as built?
5. Which host and stack is the final site going to, static files, WordPress or a framework? That decides whether the CSS should stay plain or move to components.
