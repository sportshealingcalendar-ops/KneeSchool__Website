# -*- coding: utf-8 -*-
"""Shared header and footer for the KneeSchool static pages.

There is no build step on the site itself, so this emits complete standalone
HTML files. Every path is relative with no leading slash, which keeps the pages
working from the filesystem, from a subdirectory and from a host root alike.
"""

TIERS = ["junior", "patient", "student", "mrcs", "frcs", "fellowship", "consultant"]

LEVEL_NAMES = {
    "junior": "Junior Academy",
    "patient": "Patient Academy",
    "student": "Student Academy",
    "mrcs": "MRCS Academy",
    "frcs": "FRCS (Tr and Orth) Academy",
    "fellowship": "Fellowship Academy",
    "consultant": "Consultant Masterclass",
}


def depth_bar(position, total=7, cls="depth"):
    """position is 1 based: junior is 1, consultant is 7."""
    return ('<span class="%s">' % cls
            + "".join('<i class="on"></i>' if i < position else "<i></i>"
                      for i in range(total))
            + "</span>")


def head(title, description, rel, extra_meta=""):
    return """<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>%s</title>
<meta name="description" content="%s">
<meta name="theme-color" content="#0E2A21">
%s<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;1,6..72,300&family=Source+Serif+4:opsz,wght@8..60,300;8..60,400;8..60,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="%sassets/styles.css">
</head>
<body>
""" % (title, description, extra_meta, rel)


def header(rel):
    home = "index.html" if rel == "" else rel + "index.html"
    anchor = (lambda frag: "#" + frag) if rel == "" else (lambda frag: rel + "index.html#" + frag)
    return """<header class="site-head">
  <div class="wrap head-in">
    <a class="brand" href="%s"><b>Knee</b><span>School</span></a>
    <input class="nav-toggle" type="checkbox" id="navtoggle" aria-label="Show navigation">
    <label class="burger" for="navtoggle">Menu</label>
    <nav class="nav" aria-label="Main">
      <ul>
        <li><a href="%s">Learn by level</a></li>
        <li><a href="%slevels/junior.html">Junior</a></li>
        <li><a href="%s">Encyclopaedia</a></li>
        <li><a href="%sconditions/index.html">Conditions</a></li>
        <li><a href="%s">Curriculum</a></li>
        <li><a href="%s">Practise</a></li>
        <li><a href="%s">About</a></li>
      </ul>
    </nav>
  </div>
</header>
""" % (home, anchor("levels"), rel, anchor("encyclopaedia"), rel,
       anchor("curriculum"), anchor("tools"), anchor("about"))


def footer(rel):
    anchor = (lambda frag: "#" + frag) if rel == "" else (lambda frag: rel + "index.html#" + frag)
    learn = "\n".join(
        '          <li><a href="%slevels/%s.html">%s</a></li>' % (rel, t, LEVEL_NAMES[t])
        for t in TIERS)
    return """<footer class="site-foot" id="about">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <h3>Learn</h3>
        <ul>
%s
        </ul>
      </div>
      <div>
        <h3>Reference</h3>
        <ul>
          <li><a href="%s">Anatomy</a></li>
          <li><a href="%s">Imaging</a></li>
          <li><a href="%sconditions/index.html">Conditions</a></li>
          <li><a href="%s">Rehabilitation</a></li>
          <li><a href="%s">Whole body factors</a></li>
          <li><a href="%s">Curriculum mapping</a></li>
        </ul>
      </div>
      <div>
        <h3>Clinical care</h3>
        <ul>
          <li><a href="https://www.chinmaygupte.com/">Consultant clinic</a></li>
          <li><a href="#">Imaging and injections</a></li>
          <li><a href="#">Rehabilitation programmes</a></li>
          <li><a href="#">Braces and recovery products</a></li>
        </ul>
      </div>
      <div>
        <h3>About</h3>
        <ul>
          <li><a href="%s">Editorial standards</a></li>
          <li><a href="%slevels/junior.html">For teachers and coaches</a></li>
          <li><a href="#">Authors and reviewers</a></li>
          <li><a href="#">References and sources</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
      </div>
    </div>
    <div class="legal">
      <p>KneeSchool is educational. It does not give individual medical advice and it does not replace assessment by a clinician. Seek urgent care for a hot, swollen knee with fever, a knee that cannot bear weight after injury, or new numbness in the leg.</p>
      <p>Content written for school age learners carries no advertising and no product placement.</p>
      <p>&copy; 2026 KneeSchool. All rights reserved.</p>
    </div>
  </div>
</footer>

</body>
</html>
""" % (learn, anchor("encyclopaedia"), anchor("encyclopaedia"), rel,
       anchor("encyclopaedia"), anchor("whole"), anchor("curriculum"),
       anchor("standards"), rel)


def crumb(items):
    """items is [(label, href_or_None)]; the last one carries no link."""
    parts = []
    for label, href in items:
        parts.append('<a href="%s">%s</a>' % (href, label) if href else label)
    return '<p class="crumb">' + '<span>/</span>'.join(parts) + '</p>'
