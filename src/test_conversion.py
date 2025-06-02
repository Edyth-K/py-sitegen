import unittest

from conversion import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestConversion(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a BOLD text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is a BOLD text node")

    def test_italic(self):
        node = TextNode("This is an italicized text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "This is an italicized text node")

    def test_code(self):
        node = TextNode("This is a code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, "This is a code text node")

    def test_link(self):
        node = TextNode("This is a link text node", TextType.LINK, "google.com")
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "This is a link text node")
        self.assertEqual(html_node.props, {"href":"google.com"})

    def test_image(self):
        node = TextNode("This is an image text node", TextType.IMAGE, "image.png")
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":"image.png", "alt":"This is an image text node"})



