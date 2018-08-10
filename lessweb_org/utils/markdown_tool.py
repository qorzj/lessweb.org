import markdown
from markdown.extensions.wikilinks import WikiLinkExtension
import itertools
from lessweb_org.view.frames import PanelItem, panel


NORMAL = 1
PANEL = 2

RESUME = -1
TORESET = -2
RESETED = -3


def normal_lead(token: str):
    """
    >>> normal_lead('## `Basic`')
    (2, -3)
    >>> normal_lead('## Basic')
    (1, -1)
    >>> normal_lead('`Title`')
    (1, -1)

    """
    if token is None:
        return (NORMAL, RESETED)
    elif token.startswith('#') and token.count('`') == 2:
        return (PANEL, RESETED)
    else:
        return (NORMAL, RESUME)


def panel_lead(token: str):
    """
    >>> panel_lead("  ")
    (1, -2)
    >>> panel_lead("")
    (1, -2)
    >>> panel_lead("----")
    (2, -1)

    """
    if token is None:
        return (NORMAL, RESETED)
    elif token.strip() == '':
        return (NORMAL, TORESET)
    else:
        return (PANEL, RESUME)


def rest_graph(tokens):
    """
    >>> tokens = ["# Lessweb", "> content", "", "## `Title`", "* line", ""]
    >>> for (buf, status) in rest_graph(tokens):
    ...   print(';'.join(buf))
    ...   print(status)
    # Lessweb;> content;
    1
    ## `Title`;* line
    2
    >>> tokens = ["## `Title`", "* line", "", "# Lessweb", "> content", ""]
    >>> for (buf, status) in rest_graph(tokens):
    ...   print(';'.join(buf))
    ...   print(status)
    ## `Title`;* line
    2
    # Lessweb;> content;
    1
    """
    status = NORMAL
    leader = {
        NORMAL: normal_lead,
        PANEL: panel_lead,
    }
    buf = []
    for token in itertools.chain(tokens, [None]):
        old_status = status
        status, option = leader[old_status](token)
        if option == TORESET:
            if buf:
                yield list(buf), old_status
            buf.clear()
        elif option == RESETED:
            if buf:
                yield list(buf), old_status
            buf.clear()
            buf.append(token)
        elif option == RESUME:
            buf.append(token)


def parse(md_text) -> str:
    lines = md_text.splitlines()
    ret = []
    md_wiki_ext = WikiLinkExtension(base_url='/cookbook/', end_url='')
    for (buf, status) in rest_graph(lines):
        if status == NORMAL:
            plain_text = '\n'.join(buf)
            html_text = markdown.markdown(plain_text, extensions=[
                'markdown.extensions.fenced_code',
                'markdown.extensions.nl2br',
                md_wiki_ext,
                'markdown.extensions.toc',
            ])
        elif status == PANEL:
            html_text = panel(
                title=buf[0].split('`')[1],
                items=[
                    (lambda name: PanelItem(text=name, href=f'/cookbook/{"-".join(name.split())}'))
                    (name=line.split('[[')[-1].split(']]')[0])
                    for line in buf[1:]
                ],
            ).dumps()
        else:
            raise NotImplementedError

        ret.append(html_text)

    return '\n'.join(ret)
