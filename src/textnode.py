class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        if not url:
            self.url = None
        else:
            self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode) or not isinstance(self, TextNode):
            return False
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
    )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
