from __future__ import annotations

import argparse
from typing import Sequence

import mistune
import pygments.formatters
import pygments.lexers
import pygments.util


class CodeRenderer(mistune.HTMLRenderer):
    def block_code(self, code: str, info: str | None = None) -> str:
        try:
            lexer = pygments.lexers.get_lexer_by_name(info, stripnl=False)
            cssclass = f'highlight {info}'
        except pygments.util.ClassNotFound:
            lexer = pygments.lexers.get_lexer_by_name('text', stripnl=False)
            cssclass = 'highlight'
        formatter = pygments.formatters.HtmlFormatter(cssclass=cssclass)
        return pygments.highlight(code, lexer=lexer, formatter=formatter)


def highlight(
        doc: str,
        Renderer: type[mistune.HTMLRenderer] = CodeRenderer,
) -> str:
    return mistune.Markdown(Renderer())(doc)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', default='/dev/stdin')
    args = parser.parse_args(argv)

    with open(args.filename) as f:
        hl = highlight(f.read())
        print(f'<!doctype html><html><body>{hl}</body></html>')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
