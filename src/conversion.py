from textnode import TextNode, TextType
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    text = text_node.text
    url = text_node.url
    match text_node.text_type:
        case TextType.TEXT: #This should return a LeafNode with no tag, just a raw text value.
            return LeafNode(None, text)
        case TextType.BOLD: #This should return a LeafNode with a "b" tag and the text
            return LeafNode('b', text)
        case TextType.ITALIC: #"i" tag, text
            return LeafNode('i', text)
        case TextType.CODE: #"code" tag, text
            return LeafNode('code', text)
        case TextType.LINK: #"a" tag, anchor text, and "href" prop
            return LeafNode('a', text, {"href": url})
        case TextType.IMAGE: #"img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)
            return LeafNode('img', "", {"src":url, "alt":text})
        case _:
            raise Exception("Invalid Text Type")
