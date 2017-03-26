from __future__ import absolute_import
from __future__ import unicode_literals

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
