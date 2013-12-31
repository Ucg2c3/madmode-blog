'''mm_ipy -- convert ipython notebook to markdown for madmode blog

See :func:`article_meta` for conventions for title, date, tags, etc.

.. note:: IPython.nbconvert.HTMLExporter has late-binding dependencies
          on pandoc, pygments, etc.

Acknowledgements
----------------

  * `How to Use NBConvert`__ (source__)
    Matthias Bussonnier (Carreau) Dec 01, 2013

__ http://nbviewer.ipython.org/github/Carreau/posts/blob/master/06-NBconvert-Doc-Draft.ipynb  # noqa
__ https://github.com/Carreau/posts/blob/master/06-NBconvert-Doc-Draft.ipynb

'''

from IPython.config import Config
from IPython.nbformat import current as nbformat


def main(argv, arg_rd, arg_wr, HTMLExporter,
         encoding='utf-8'):
    '''
    .. note:: HTMLExporter includes access to run pandoc etc.
    '''
    notebook_fn, article_fn = argv[1:3]

    notebook_txt = arg_rd(notebook_fn).read()
    with arg_wr(article_fn) as outfp:
        for chunk in article_of(notebook_txt, HTMLExporter):
            outfp.write(chunk.encode(encoding))


def article_of(notebook_txt, HTMLExporter):
    notebook = nbformat.reads_json(notebook_txt)

    hide, meta = article_meta(notebook)
    for ix in sorted(hide, reverse=True):
        del notebook.worksheets[0].cells[ix]

    for n, v in meta:
        yield '%s: %s\n' % (n, v)
    yield '\n'

    exportHtml = HTMLExporter(config=Config({'HTMLExporter':
                                             {'default_template': 'basic'}}))

    body, resources = exportHtml.from_notebook_node(notebook)
    # [txt[:100] for txt in resources['inlining']['css']]

    yield body


def article_meta(notebook,
                 meta_start='<pre class="about yaml">',
                 meta_end='</pre>'):
    '''Collect article metadata from a notebook.

    The title is taken from the (first) heading level 1 cell.

    Other metadata is taken from the (first) cell that starts with::

      >>> print article_meta.func_defaults[0]
      <pre class="about yaml">

    The closing tag is ignored::

      >>> print article_meta.func_defaults[1]
      </pre>
    '''
    def find_cell(test):
        return ((i, cell['source'])
                for i, cell in enumerate(notebook.worksheets[0].cells)
                if test(cell)).next()

    h1_ix, h1 = find_cell(
        lambda cell: (cell['cell_type'] == 'heading'
                      and cell['level'] == 1))

    meta_ix, meta_txt = find_cell(
        lambda cell: cell['source'].startswith(meta_start))

    meta = grok_yaml(meta_txt, [meta_start, meta_end])

    return [h1_ix, meta_ix], [('title', repr(str(h1)))] + meta


def grok_yaml(txt, excludes=[]):
    '''Quick-n-dirty YAML parser.

    >>> grok_yaml("""<pre>
    ... date: 2001-01-01
    ... tags: ['travel', 'humor']
    ... </pre>""", excludes=['<'])
    [('date', '2001-01-01'), ('tags', "['travel', 'humor']")]

    .. note:: TODO: handle continuation lines properly.

    >>> grok_yaml("""<pre>
    ... summary: What I did
    ...   this summer.
    ... </pre>""", excludes=['<'])
    [('summary', 'What I did'), ('  this summer.',)]
    '''
    return [tuple(line.split(': ', 1))  # name: value
            for line in txt.split('\n')
            if not [line for ex in excludes if line.startswith(ex)]]


if __name__ == '__main__':
    def _with_caps():
        '''Trusted computing base to get capabilities and call main().

        This follows an `object capability discipline for python`__.

        __ http://www.madmode.com/2013/python-capability-idioms-part-1.html
        '''
        from sys import argv
        from IPython.nbconvert import HTMLExporter

        def arg_rd(n):
            if n not in argv:
                raise IOError
            return open(n)

        def arg_wr(n):
            if n not in argv:
                raise IOError
            return open(n, 'w')

        main(argv[:], arg_rd, arg_wr, HTMLExporter)

    _with_caps()
