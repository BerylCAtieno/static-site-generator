class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("This function has yet to be implemented")

    def props_to_html(self):
        attributes = [f'{key}="{value}"' for key, value in self.props.items()]
        return ' '.join(attributes)


