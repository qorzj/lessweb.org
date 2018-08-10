from lessweb_org.service.cookbook import CookbookService


def home(serv: CookbookService) -> str:
    name = 'Home'
    html_text = serv.get_html(name)
    return html_text


def article(serv: CookbookService, name) -> str:
    name = name.replace('_', '-')
    html_text = serv.get_html(name)
    return html_text
