class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""
        propsstr = ""
        for item in self.props.items():
            propsstr += f" {item[0].lower()}=\"{item[1]}\""
        return propsstr

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("no value provided in leaf node")
        if self.tag is None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("no tag provided")
        if self.children is None:
            raise ValueError("no children provided in parent node")
        childrenstr = "".join(map(lambda c: c.to_html(), self.children))
        return f"<{self.tag}{self.props_to_html()}>" + childrenstr + f"</{self.tag}>"
