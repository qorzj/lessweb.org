from lessweb_org.service.cookbook import CookbookService


def home(serv: CookbookService):
    name = 'Home'
    html_text = serv.get_html(name)
    return html_text


def article(serv: CookbookService, name):
    html_text = serv.get_html(name)
    return html_text
