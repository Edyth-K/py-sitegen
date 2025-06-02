import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        html_node = HTMLNode("p", "This is a paragraph",
                             None, {"href": "https://www.google.com",
                                    "target": "_blank",}
                            )
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(expected, html_node.props_to_html())

    def test_repr(self):
        html_node = HTMLNode("p", "This is a paragraph",
                        None, {"href": "https://www.google.com",
                            "target": "_blank",}
                    )
        expected = ('HTMLNode:\n'+
                    'Tag: p\n'+
                    'Value: This is a paragraph\n'+
                    'Children: None\n'+
                    "Props: {'href': 'https://www.google.com', 'target': '_blank'}"
                    )
        self.assertEqual(repr(html_node), expected)
    
    def test_props_to_html_on_empty_node(self):
        html_node = HTMLNode()
        self.assertEqual("",html_node.props_to_html())