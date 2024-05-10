import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

#    def __init__(self, tag=None, value=None, children=None, props=None):

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("CSS", "20", "child", {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("CSS", "20", "child", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
