from .pydom import Node as D


def pageFrame(file, *divs):
    if file:
        modname = file.split('/')[-1].rsplit('.', 1)[0]
        modjs = D('script', '', Src=f'/static/__javascript__/{modname}.js')
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
            D(Href='https://res.wx.qq.com/open/libs/weui/1.1.2/weui.min.css', Rel='stylesheet', Type='text/css').Link,
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
