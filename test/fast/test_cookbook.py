from unittest import TestCase

from lessweb.utils import Mock, DEFAULT
from lessweb_org.service.cookbook import CookbookService
from lessweb_org import controller
import lessweb_org.controller.cookbook


class TestCookbook(TestCase):
    def test_home(self):
        serv = CookbookService()
        serv.get_html = Mock()
        serv.get_html.side_effect = lambda name: [self.assertEqual(name, 'Home')] and name
        html_text = controller.cookbook.home(serv)
        self.assertEqual(html_text, 'Home')

    def test_article(self):
        serv = CookbookService()
        serv.get_html = Mock()
        serv.get_html.side_effect = lambda name: name
        html_text = controller.cookbook.article(serv, 'Hello World')
        self.assertEqual(html_text, 'Hello World')
