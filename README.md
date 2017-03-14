markdown-code-blocks
====================

A stupid simple bit of code which combines [mistune][mistune] and
[pygments][pygments] to convert markdown into html.  Very similar to github
markdown, but for python.


## Installation

`pip install markdown-code-blocks`

## Usage

The library provides a single function `highlight` which takes in a markdown
string and returns html.


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
