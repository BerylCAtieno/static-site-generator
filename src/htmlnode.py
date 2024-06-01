class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
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
    def __init__(self, tag=None, value=None, props=None):
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

    def __init__(self, tag, children, props=None):
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
