# This Python file uses the following encoding: utf-8

from unittest import TestCase
from panflute import *

from helper import verify_conversion

def test_unlisted():
    verify_conversion(
        '''
Header {.unlisted}
======
        ''',
        '''
---
header-includes:
- '\\let\\oldaddcontentsline\\addcontentsline'
---

\\let\\oldaddcontentsline\\addcontentsline

\\renewcommand{\\addcontentsline}[3]{}
Header {#header .unlisted}
======

\\renewcommand{\\addcontentsline}[3]{\\oldaddcontentsline{#1}{#2}{#3}}
        ''',
        'latex'
    )

def test_meta_simple():
    verify_conversion(
        '''
---
pandoc-latex-unlisted: [myclass]
---

Header {.myclass}
======
        ''',
        '''
---
header-includes:
- '\\let\\oldaddcontentsline\\addcontentsline'
pandoc-latex-unlisted:
- myclass
---

\\let\\oldaddcontentsline\\addcontentsline

\\renewcommand{\\addcontentsline}[3]{}
Header {#header .myclass}
======

\\renewcommand{\\addcontentsline}[3]{\\oldaddcontentsline{#1}{#2}{#3}}
        ''',
        'latex'
    )

def test_meta_multiple():
    verify_conversion(
        '''
---
pandoc-latex-unlisted: [[myclass1, myclass2]]
---

Header {.myclass1 .myclass2}
======
        ''',
        '''
---
header-includes:
- '\\let\\oldaddcontentsline\\addcontentsline'
pandoc-latex-unlisted:
- - myclass1
  - myclass2
---

\\let\\oldaddcontentsline\\addcontentsline

\\renewcommand{\\addcontentsline}[3]{}
Header {#header .myclass1 .myclass2}
======

\\renewcommand{\\addcontentsline}[3]{\\oldaddcontentsline{#1}{#2}{#3}}
        ''',
        'latex'
    )

def test_header_includes1():
    verify_conversion(
        '''
---
header-includes: \\usepackage{fancyhdr}
---
Header {.unlisted}
======
        ''',
        '''
---
header-includes:
- '\\usepackage{fancyhdr}'
- '\\let\\oldaddcontentsline\\addcontentsline'
---

\\usepackage{fancyhdr}

\\let\\oldaddcontentsline\\addcontentsline

\\renewcommand{\\addcontentsline}[3]{}
Header {#header .unlisted}
======

\\renewcommand{\\addcontentsline}[3]{\\oldaddcontentsline{#1}{#2}{#3}}
        ''',
        'latex'
    )

def test_header_includes2():
    verify_conversion(
        '''
---
header-includes: |
    \\usepackage{fancyhdr}
    \\pagestyle{fancy}
---
Header {.unlisted}
======
        ''',
        '''
---
header-includes:
- |
    \\usepackage{fancyhdr}
    \\pagestyle{fancy}
- '\\let\\oldaddcontentsline\\addcontentsline'
---

\\usepackage{fancyhdr}
\\pagestyle{fancy}

\\let\\oldaddcontentsline\\addcontentsline

\\renewcommand{\\addcontentsline}[3]{}
Header {#header .unlisted}
======

\\renewcommand{\\addcontentsline}[3]{\\oldaddcontentsline{#1}{#2}{#3}}
        ''',
        'latex'
    )

