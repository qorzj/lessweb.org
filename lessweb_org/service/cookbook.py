from functools import lru_cache
import os

from lessweb import Service, NotFound
from lessweb_org.utils import markdown_tool


@lru_cache(maxsize=128)
def get_cached_html(name):
    filename = f'{CookbookService.wiki_path}/{name}.md'
    try:
        md_text = open(filename).read()
    except:
        raise NotFound(text='not found')
    html_text = markdown_tool.parse(md_text)
    return html_text


class CookbookService(Service):
    wiki_path = 'data/lessweb.wiki'

    def get_html(self, name) -> str:
        return get_cached_html(name)

    def fetch_wiki(self):
        if os.path.exists(self.wiki_path):
            os.system('cd data && git pull')
        else:
            os.system('cd data && git clone https://github.com/qorzj/lessweb.wiki.git')
        get_cached_html.cache_clear()
