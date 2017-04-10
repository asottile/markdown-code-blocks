from __future__ import absolute_import
from __future__ import unicode_literals

import argparse
import io

import mistune
import pygments.formatters
import pygments.lexers
import pygments.util


class CodeRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        try:
            lexer = pygments.lexers.get_lexer_by_name(lang, stripnl=False)
        except pygments.util.ClassNotFound:
            lexer = pygments.lexers.get_lexer_by_name('text', stripnl=False)
        formatter = pygments.formatters.HtmlFormatter()
        return pygments.highlight(code, lexer=lexer, formatter=formatter)


def highlight(doc, Renderer=CodeRenderer):
    return mistune.Markdown(Renderer(escape=True, hard_wrap=False))(doc)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', default='/dev/stdin')
    args = parser.parse_args(argv)

    with io.open(args.filename) as f:
        hl = highlight(f.read())
        print('<!doctype html><html><body>{}</body></html>'.format(hl))


if __name__ == '__main__':
    exit(main())
