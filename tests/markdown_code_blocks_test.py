from markdown_code_blocks import CodeRenderer
from markdown_code_blocks import highlight
from markdown_code_blocks import main


def test_simple_markdown():
    ret = highlight('## ohai\n')
    assert ret == '<h2>ohai</h2>\n'


def test_highlight_python():
    ret = highlight(
        '```python\n'
        'print("hello world")\n'
        '```\n',
    )
    assert ret == (
        '<div class="highlight python"><pre>'
        '<span></span>'
        '<span class="nb">print</span>'
        '<span class="p">(</span>'
        '<span class="s2">&quot;hello world&quot;</span>'
        '<span class="p">)</span>\n'
        '</pre></div>\n'
    )


def test_highlight_plain_text():
    ret = highlight(
        '```\n'
        'this is plain text, such class.\n'
        '```\n',
    )
    assert ret == (
        '<div class="highlight"><pre>'
        '<span></span>'
        'this is plain text, such class.\n'
        '</pre></div>\n'
    )


def test_custom_renderer():
    class MyRenderer(CodeRenderer):
        def block_code(self, *args):
            return 'nope'
    ret = highlight(
        'hello\n'
        '```\n'
        'world\n'
        '```\n',
        Renderer=MyRenderer,
    )
    assert ret == '<p>hello</p>\nnope'


def test_main(capsys, tmpdir):
    f = tmpdir.join('f')
    f.write('## ohai\n')
    main((f.strpath,))
    out, _ = capsys.readouterr()
    assert out == '<!doctype html><html><body><h2>ohai</h2>\n</body></html>\n'
