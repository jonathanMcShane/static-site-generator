class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f" 'tag': {self.tag}, 'value': {self.value}, 'children': {self.children}, 'props': {self.props}"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        html_props = ""
        for key in self.props:
            html_props += (f' {key}="{self.props[key]}"')
        return html_props
    
class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("Invalid HTML: No value")
        if self.tag == None:
            return self.value
        return f'<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>'
    
class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Invalid HTML: No tag")
        if self.children == None:
            raise ValueError("Invalid HTML: No children")

        html_children = ""
        for child in self.children:
            html_children += child.to_html()
        return f"<{self.tag}{super().props_to_html()}>{html_children}</{self.tag}>"
    
     

    

    