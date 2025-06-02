class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        """
        tag - A string representing the HTML tag name 
            (e.g. "p", "a", "h1", etc.)
        value - A string representing the value of the HTML tag 
            (e.g. the text inside a paragraph)
        children - A list of HTMLNode objects representing 
            the children of this node
        props - A dictionary of key-value pairs representing 
            the attributes of the HTML tag. For example, a 
            link (<a> tag) might have {"href": "https://www.google.com"}
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        output = ""
        try:
            for attribute in self.props:
                output += f' {attribute}="{self.props[attribute]}"'
            return output
        except TypeError as e:
            return output
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("leaf node must have a value")
        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("parent node must have a tag")
        if self.children == None:
            raise ValueError("parent node must have children")
        children_values = ""
        for child in self.children:
            if child.value == None and child.children == None:
                raise ValueError("all children of parent node must have values or children")
            children_values += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_values}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"