class HTMLNode:
    def __init__(self, tag:str=None, value:str=None, children:list=None, props:dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("This function has yet to be implemented")

    def props_to_html(self):
        if not self.props:
            return ''
        attributes = [f'{key}="{value}"' for key, value in self.props.items()]
        return ' '.join(attributes)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag:str=None, value:str=None, props:dict=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")

        if self.tag is None:
            return self.value
        
        attributes = self.props_to_html()
        if attributes:
            return f'<{self.tag} {attributes}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):

    def __init__(self, tag:str, children:list, props:dict=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag")
        if not children:
            raise ValueError("ParentNode must have at least one child")
        super().__init__(tag, None, children, props)
    
    def to_html(self):

        if self.tag == None:
            raise ValueError("Parent note must have a tag")
        
        if not self.children:
            raise ValueError("ParentNode must have at least one child")

        children_html = ''.join(child.to_html() for child in self.children)
        attributes = self.props_to_html()
        if attributes:
            return f'<{self.tag} {attributes}>{children_html}</{self.tag}>'
        else:
            return f'<{self.tag}>{children_html}</{self.tag}>'

def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        return LeafNode(tag=None, value=text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == "italic":
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == "code":
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == "link":
        if text_node.url is None:
            raise ValueError("Link type TextNode must have a URL")
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    elif text_node.text_type == "image":
        if text_node.url is None or text_node.alt is None:
            raise ValueError("Image type TextNode must have a URL and alt text")
        return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.alt})
    else:
        raise ValueError(f"Unknown text type: {text_node.text_type}")