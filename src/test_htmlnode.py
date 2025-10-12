import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(tag="div", value="Hello", children=[], props={"class": "container"})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=Hello, children=[], props={'class': 'container'})")

    def test_props_to_html(self):
        node = HTMLNode(tag="a", value="Link", props={"href": "http://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="http://example.com" target="_blank"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()