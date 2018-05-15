#!/usr/bin/env python

"""
Pandoc filter for unlisting user defined headers in LaTeX
"""

from panflute import *

def header(elem, doc):
    # Is it in the right format and is it an Header?
    if doc.format == 'latex' and isinstance(elem, Header):
        classes = set(elem.classes)
        for current in doc.list_classes:
            if current <= classes:
                return [
                    RawBlock('\\renewcommand{\\addcontentsline}[3]{}', 'tex'),
                    elem,
                    RawBlock('\\renewcommand{\\addcontentsline}[3]{\\oldaddcontentsline{#1}{#2}{#3}}', 'tex'),
                ]

def prepare(doc):
    doc.list_classes = [set(['unlisted'])]
    metadata = doc.get_metadata()
    if 'pandoc-latex-unlisted' in metadata and isinstance(metadata['pandoc-latex-unlisted'], list):
        doc.list_classes = []
        for classes in metadata['pandoc-latex-unlisted']:
            try:
                type = unicode
            except NameError:
                type = str
            if isinstance(classes, type):
                doc.list_classes.append(set([classes]))
            elif isinstance(classes, list):
                doc.list_classes.append(set(classes))

def finalize(doc):
    # Add header-includes if necessary
    if 'header-includes' not in doc.metadata:
        doc.metadata['header-includes'] = MetaList()
    # Convert header-includes to MetaList if necessary
    elif not isinstance(doc.metadata['header-includes'], MetaList):
        doc.metadata['header-includes'] = MetaList(doc.metadata['header-includes'])
    doc.metadata['header-includes'].append(MetaInlines(RawInline('\\let\\oldaddcontentsline\\addcontentsline', 'tex')))
    
def main(doc = None):
    return run_filter(header, prepare = prepare, doc = doc, finalize = finalize)

if __name__ == '__main__':
    main()

