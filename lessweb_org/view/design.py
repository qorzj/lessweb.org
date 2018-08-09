from .frames import pageFrame, panel, PanelItem
from .pydom import Node as D


def homePage(_):
    return pageFrame(
        None,
        D(
            D('大标题').H1,
            D('lessweb fullstack web framework.').Section,
        ).Article,
        panel(
            title='基础',
            items=[
                PanelItem(text='安装', href='#'),
                PanelItem(text='Hello World', href='#'),
                PanelItem(text='处理请求', href='#'),
                PanelItem(text='Path Variable', href='#'),
                PanelItem(text='重定向', href='#'),
                PanelItem(text='上传文件', href='#'),
            ],
        ),
        panel(
            title='进阶',
            items=[
                PanelItem(text='上下文对象', href='#'),
                PanelItem(text='获取POST请求的raw data', href='#'),
                PanelItem(text='Cookie', href='#'),
                PanelItem(text='拦截器', href='#'),
                PanelItem(text='参数改名与传递', href='#'),
                PanelItem(text='后端模板', href='#'),
            ],
        ),
    )
