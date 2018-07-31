from .frames import pageFrame
from .pydom import Node as D


def homePage(_):
    return pageFrame(
        None,
        D(
            D('大标题').H1,
            D('lessweb fullstack web framework.').Section,
        ).Article,
    )
