class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        props_html = []
        for key, value in self.props.items():
            # Handle boolean attributes without quotes
            if isinstance(value, bool):
                if value:
                    props_html.append(f"{key}")  # Add key for boolean attributes (e.g., checked)
            else:
                # Escape quotes within values to prevent breaking the attribute
                escaped_value = value.replace('"', '&quot;')  # Escape double quotes
                props_html.append(f'{key}="{escaped_value}"')
        props_to_html_result = " ".join(props_html)
        return props_to_html_result.lstrip(" ")
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        if not isinstance(other, HTMLNode) or not isinstance(self, HTMLNode):
            return False
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == self.props
    )

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if not value:
            raise ValueError("LeafNode requires a value argument")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("No value for LeafNode")
        if self.tag == None:
            return self.value
        else:
            if self.props:
                html_result = f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
            else:
                html_result = f"<{self.tag}>{self.value}</{self.tag}>"
            return html_result


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not children:
            raise ValueError("ParentNode requires a children argument")
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag for ParentNode")
        if self.children == None:
            raise ValueError("No children for ParentNode")
        html_result = ""
        if self.props:
            html_result += f"<{self.tag} {self.props_to_html()}>"
        else:
            html_result +=f"<{self.tag}>"
        for child in self.children:
            html_result += child.to_html()
        html_result += f"</{self.tag}>"
        return html_result

                
# node = LeafNode("p", "This is a paragraph of text.")
# node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
# html_string = node.to_html()
# print(html_string)
# html_string = node2.to_html()
# print(html_string)

# node2 = ParentNode(
#     "p",
#     [
#         LeafNode("b", "Bold text"),
#         LeafNode(None, "Normal text"),
#         LeafNode("i", "italic text"),
#         LeafNode(None, "Normal text"),
#     ],
# )

# html_string = node2.to_html()
# print(html_string)

