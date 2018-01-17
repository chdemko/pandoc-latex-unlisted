# pandoc-latex-unlisted
[![Build Status](https://img.shields.io/travis/chdemko/pandoc-latex-unlisted/0.1.0.svg)](https://travis-ci.org/chdemko/pandoc-latex-unlisted/branches)
[![Coveralls](https://img.shields.io/coveralls/github/chdemko/pandoc-latex-unlisted/0.1.0.svg)](https://coveralls.io/github/chdemko/pandoc-latex-unlisted?branch=0.1.0)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/chdemko/pandoc-latex-unlisted.svg)](https://scrutinizer-ci.com/g/chdemko/pandoc-latex-unlisted/)
[![PyPI version](https://img.shields.io/pypi/v/pandoc-latex-unlisted.svg)](https://pypi.org/project/pandoc-latex-unlisted/)
[![PyPI format](https://img.shields.io/pypi/format/pandoc-latex-unlisted/0.1.0.svg)](https://pypi.org/project/pandoc-latex-unlisted/0.1.0/)
[![License](https://img.shields.io/pypi/l/pandoc-latex-unlisted/0.1.0.svg)](https://raw.githubusercontent.com/chdemko/pandoc-latex-unlisted/0.1.0/LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/pandoc-latex-unlisted.svg)](https://pypi.org/project/pandoc-latex-unlisted/)
[![Python version](https://img.shields.io/pypi/pyversions/pandoc-latex-unlisted.svg)](https://pypi.org/project/pandoc-latex-unlisted/)
[![Development Status](https://img.shields.io/pypi/status/pandoc-latex-unlisted.svg)](https://pypi.org/project/pandoc-latex-unlisted/)

*pandoc-latex-unlisted* is a [pandoc] filter for unlisting some headers in the table of contents in *LaTeX*.

[pandoc]: http://pandoc.org/

Documentation
-------------

See the [wiki pages](https://github.com/chdemko/pandoc-latex-unlisted/wiki).

Usage
-----

To apply the filter, use the following option with pandoc:

    --filter pandoc-latex-unlisted

Installation
------------

*pandoc-latex-unlisted* requires [python], a programming language that comes pre-installed on linux and Mac OS X, and which is easily installed [on Windows]. Either python 2.7 or 3.x will do.

Install *pandoc-latex-unlisted* as root using the bash command

    pip install pandoc-latex-unlisted

To upgrade to the most recent release, use

    pip install --upgrade pandoc-latex-unlisted

`pip` is a script that downloads and installs modules from the Python Package Index, [PyPI].  It should come installed with your python distribution. If you are running linux, `pip` may be bundled separately. On a Debian-based system (including Ubuntu), you can install it as root using

    apt-get update
    apt-get install python-pip

[python]: https://www.python.org
[on Windows]: https://www.python.org/downloads/windows
[PyPI]: https://pypi.org


Getting Help
------------

If you have any difficulties with *pandoc-latex-unlisted*, please feel welcome to [file an issue] on github so that we can help.

[file an issue]: https://github.com/chdemko/pandoc-latex-unlisted/issues

