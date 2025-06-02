import unittest

from htmlnode import HTMLNode, LeafNode

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

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")