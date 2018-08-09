from unittest import TestCase

from lessweb_org.utils import markdown_tool


class TestParse(TestCase):
    def test_parse_normal_markdown(self):
        md_text = '### title'
        html_text = markdown_tool.parse(md_text)
        self.assertEqual(html_text, '<h3>title</h3>')

    def test_parse_weui_markdown(self):
        md_text = """### title
* line1
* line2
## `Model`
* line3
* line4 
        """
        html_text = markdown_tool.parse(md_text)
        self.assertIn('weui-panel__hd', html_text)
