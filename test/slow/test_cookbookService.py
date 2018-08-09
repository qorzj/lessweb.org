import os
from unittest import TestCase
from unittest.mock import patch, Mock

from lessweb_org.service.cookbook import CookbookService


class TestCookbookService(TestCase):
    @patch('lessweb_org.utils.markdown_tool')
    def test_fetch_wiki_and_get_html(self, markdown_tool_patch):
        serv = CookbookService()
        # test fetch_wiki()
        serv.fetch_wiki()
        self.assertTrue(os.path.isfile(f'{serv.wiki_path}/Home.md'))
        # test get_html()
        markdown_tool_patch.parse = Mock()
        markdown_tool_patch.parse.side_effect = lambda text: text
        html_text = serv.get_html('Home')
        self.assertIn('嘞是web', html_text)
