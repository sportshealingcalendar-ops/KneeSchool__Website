# KneeSchool.com

Static front end and content pipeline for KneeSchool, a spiral knee curriculum
that teaches the same topic seven times at increasing depth.

```
index.html        the homepage
assets/styles.css one shared stylesheet, no build step, no JavaScript
levels/           seven level landing pages, one per tier
conditions/       the conditions library and the ACL template article
tools/            check_site.py, the whole site check
pipeline/         the three agent content pipeline: prompts, config, Lambdas,
                  Step Functions definition, SAM template, tests
docs/             the handover and the team pack that drive both
```

## The seven tiers

Junior, Patient, Student, MRCS, FRCS (Tr and Orth), Fellowship, Consultant
Masterclass. Each tier assumes the one below it and adds a layer rather than
repeating it.

## Site

`index.html` has no build step. Open it, or serve the directory:

```bash
python3 -m http.server 8000
```

Check every page at once:

```bash
python3 tools/check_site.py
```

That covers tag balance, `lang`, em and en dashes, space hyphen space, the
banned phrase and UK spelling rules from the pipeline config, and whether every
relative link and in-page anchor actually resolves. Exit code 1 on any failure.

Then check by eye at 375px, 768px and 1440px. Single page structure check:

```bash
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
print("dashes:", '—' in txt or '–' in txt)
EOF
```

## Pipeline

```bash
make -C pipeline test     # 47 tests, no AWS account needed
make -C pipeline lint DRAFT=path/to/draft.md
```

See `pipeline/README.md` for the architecture, the deployment steps and the
decisions that are still open.

## House rules

British English. No em dashes and no en dashes. Short sentences, one idea each.
Sentence case headings. Buttons name the action. No unsupported clinical claims
and no invented references. Every clinical page carries the educational
disclaimer and the red flag advice.

Consultant review is mandatory before publication and cannot be bypassed. The
state machine enforces that structurally, and `pipeline/tests/` asserts it.
