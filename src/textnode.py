from enum import Enum

from htmlnode import LeafNode, ParentNode

class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    LINK = "link"
    CODE = "code"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self,other):
        if not isinstance(other, TextNode):
            return False
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.PLAIN:
        return LeafNode("", text_node.text, TextType.PLAIN)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text, TextType.BOLD)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text, TextType.ITALIC)
    elif text_node.text_type == TextType.LINK:
        return LeafNode(text_node.text, TextType.LINK, text_node.url)
    elif text_node.text_type == TextType.CODE:
        return ParentNode("code", [LeafNode(text_node.text, TextType.PLAIN)])
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("", TextType.IMAGE, text_node.url)
    else:
        raise ValueError("Unknown TextType")