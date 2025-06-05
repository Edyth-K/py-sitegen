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

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid Markdown")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def md_to_text_node(md):
    '''
    Converts raw markdown to TextNode

    For example, given the string:
        
        This is text with a **bolded phrase** in the middle

    Return:

        [
        TextNode("This is text with a ", TextType.TEXT),
        TextNode("bolded phrase", TextType.BOLD),
        TextNode(" in the middle", TextType.TEXT),
        ]
    '''
    pass

