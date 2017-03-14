from __future__ import absolute_import
from __future__ import unicode_literals

from markdown_code_blocks import highlight


def test_simple_markdown():
    ret = highlight('## ohai\n')
    assert ret == '<h2>ohai</h2>\n'


def test_highlight_python():
    ret = highlight(
        '```python\n'
        'print("hello world")\n'
        '```\n'
    )
    assert ret == (
        '<div class="highlight"><pre>'
        '<span></span>'
        '<span class="k">print</span>'
        '<span class="p">(</span>'
        '<span class="s2">&quot;hello world&quot;</span>'
        '<span class="p">)</span>\n'
        '</pre></div>\n'
    )


def test_highlight_plain_text():
    ret = highlight(
        '```\n'
        'this is plain text, such class.\n'
        '```\n'
    )
    assert ret == (
        '<div class="highlight"><pre>'
        '<span></span>'
        'this is plain text, such class.\n'
        '</pre></div>\n'
    )
