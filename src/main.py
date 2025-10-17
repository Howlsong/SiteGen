from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
def main():
    dummy=LeafNode("a", TextType.PLAIN, "c")
    print(dummy.to_html())

main()