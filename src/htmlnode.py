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
        return (("HTMLNode:\n") +
                (f"Tag: {self.tag}\n") +
                (f"Value: {self.value}\n") +
                (f"Children: {self.children}\n") +
                (f"Props: {self.props}")
        )