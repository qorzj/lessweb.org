from .frames import pageFrame, panel, PanelItem
from .pydom import Node as D


def homePage(html_text):
    return pageFrame(
        None,
        D(html_text).Article,
    )


def articlePage(html_text):
    return pageFrame(
        None,
        D(html_text).Article,
    )
