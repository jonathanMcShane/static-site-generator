from textnode import TextNode, split_nodes_delimiter
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    node = TextNode("This is text with a `code block` word", "text")
    new_nodes = split_nodes_delimiter([node], "`", "code")

    print(new_nodes)

    

main()