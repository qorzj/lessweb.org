# __pragma__('kwargs')
"""
Dom Element
"""

def uncapitalize_name(name):
    """
        >>> uncapitalize_name("Href")
        'href'
        >>> uncapitalize_name("HttpEquiv")
        'http-equiv'

    """
    buf = []
    for c in name:
        if 'A' <= c <= 'Z' and len(buf):
            buf.append('-')
        buf.append(c)
    return ''.join(buf).lower()


class Node:
    JSVOID = 'javascript:void(0)'
    WIDOW = '__Node::Widow__'

    def __init__(self, *children, **attrs):
        self.tag = 'div'
        self.children = children
        self.attrs = dict(attrs)

    def __getattr__(self, key):
        self.tag = uncapitalize_name(key)
        return self

    def _dump_head(self):
        sb = [self.tag]
        for key, value in self.attrs.items():
            if value is not None:
                sb.append(' {}={}'.format(uncapitalize_name(key), repr(value)))
            elif value == Node.WIDOW:
                sb.append(' {}'.format(uncapitalize_name(key)))
        return ''.join(sb)

    def dumps(self):
        sb = []
        if self.tag.lower() == 'html':
            sb.append('<!DOCTYPE html>\n')
        if len(self.children):
            sb.append('<{}>'.format(self._dump_head()))
            for child in self.children:
                if isinstance(child, str):
                    sb.append(child)
                elif isinstance(child, Node):
                    sb.append(child.dumps())
                else:
                    sb.append(str(child))
            sb.append('</{}>'.format(self.tag))
            return ''.join(sb)
        else:
            return '<{}/>'.format(self._dump_head())


# __pragma__('nokwargs')
