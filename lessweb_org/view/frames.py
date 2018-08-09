from .pydom import Node as D


def pageFrame(file, *divs):
    if file:
        modname = file.split('/')[-1].rsplit('.', 1)[0]
        modjs = D('', Src=f'/static/__javascript__/{modname}.js').Script
    else:
        modjs = ''
    return D(
        D(
            D(Charset='UTF-8').Meta,
            D(Rel='shortcut icon', Type='image/x-icon', Href='/static/favicon.png', Media='screen').Link,
            D(HttpEquiv='Cache-Control', Content='no-cache, no-store, must-revalidate').Meta,
            D(HttpEquiv='Pragma', Content='no-cache').Meta,
            D(HttpEquiv='Expires', Content='0').Meta,
            D('Lessweb: Python Fullstack Web Framework').Title,
            D(Href='https://res.wx.qq.com/open/libs/weui/1.1.3/weui.min.css', Rel='stylesheet', Type='text/css').Link,
            D('', Src='/static/js/zepto.min.js').Script,
            D(
                """
                body {
                    position: relative;
                    width: 100%;
                    height: 100vh;
                    max-width: 640px;
                    margin: 0 auto;
                    margin-bottom: 1.33rem;
                    background-color: #f8f8f8;
                }
                """,
            ).Style,
        ).Head,
        D(
            *divs,
            D('', Src='https://res.wx.qq.com/open/libs/weuijs/1.1.3/weui.min.js').Script,
            modjs,
        ).Body,
    ).Html


class PanelItem:
    def __init__(self, text, href):
        self.text = text
        self.href = href


def panel(*, title, items):
    return D(
        D(title, Class="weui-panel__hd", Style="font-size:15px").Div,
        D(
            D(
                D(
                    *[
                        D(
                            D(item.text, Class="weui-cell__bd weui-cell_primary"),
                            D(Class="weui-cell__ft").Span,
                            Href=item.href,
                            Class="weui-cell weui-cell_access",
                        ).A
                        for item in items
                    ],
                    Class="weui-cells",
                ),
                Class="weui-media-box weui-media-box_small-appmsg",
            ),
            Class="weui-panel__bd",
        ),
        Class="weui-panel",
    )