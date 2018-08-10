from .pydom import Node as D


def footer():
    return D(
        D(
            D('首页', Href='/', Class="weui-footer__link").A,
            D('Github', Href='https://github.com/qorzj/lessweb', Class="weui-footer__link").A,
            Class="weui-footer__links",
        ).P,
        D(
            'Copyright &copy; 2018 lessweb.org<br/><br/><br/>',
            Class="weui-footer__text",
        ).P,
        Class="weui-footer",
    )


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
            D(Name='apple-mobile-web-app-capable', Content='yes').Meta,
            D(Name='apple-touch-fullscreen', Content='yes').Meta,
            D(Name='viewport', Content='width=device-width, initial-scale=1,maximum-scale=1,user-scalable=no').Meta,  # 响应式布局的关键
            D(HttpEquiv='Cache-Control', Content='no-cache, no-store, must-revalidate').Meta,
            D(HttpEquiv='Pragma', Content='no-cache').Meta,
            D(HttpEquiv='Expires', Content='0').Meta,
            D('Lessweb: Python Fullstack Web Framework').Title,
            D(Href='https://res.wx.qq.com/open/libs/weui/1.1.3/weui.min.css', Rel='stylesheet', Type='text/css').Link,
            D(Href='/static/css/site.css', Rel='stylesheet', Type='text/css').Link,
            D(Href='//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/styles/default.min.css', Rel='stylesheet', Type='text/css').Link,
            D('', Src='/static/js/zepto.min.js').Script,
            D('', Src='//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/highlight.min.js').Script,
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
            footer(),
            D('', Src='https://res.wx.qq.com/open/libs/weuijs/1.1.3/weui.min.js').Script,
            modjs,
            D('hljs.initHighlightingOnLoad();').Script,
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
