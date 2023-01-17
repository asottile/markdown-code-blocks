[![build status](https://github.com/asottile/markdown-code-blocks/actions/workflows/main.yml/badge.svg)](https://github.com/asottile/markdown-code-blocks/actions/workflows/main.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/asottile/markdown-code-blocks/main.svg)](https://results.pre-commit.ci/latest/github/asottile/markdown-code-blocks/main)

markdown-code-blocks
====================

A stupid simple bit of code which combines [mistune][mistune] and
[pygments][pygments] to convert markdown into html.  Very similar to github
markdown, but for python.


## Installation

```bash
pip install markdown-code-blocks
```

## Usage

The library provides a single function `highlight` which takes in a markdown
string and returns html.

You can also use the cli `markdown-code-blocks-highlight`.  It optionally
takes a single filename (defaulting to stdin) and writes to stdout.

For example:

`markdown-code-blocks-highlight f.md > f.html`


## pygments css

I'd suggest grabbing a theme file from [pygments-css][pygments-css]
(or any other provider of pygments themes -- if you google there's a bunch of
them).

This library will use the class `.highlight` so be sure to change out whatever
class the theme uses with that.

Most themes (for whatever reason) don't add styles for diff display.  I
usually do something like this:

```css
.highlight .gi { color: #070; }
.highlight .gd { color: #911; }
```

[mistune]: https://github.com/lepture/mistune
[pygments]: http://pygments.org/
[pygments-css]: https://github.com/richleland/pygments-css
