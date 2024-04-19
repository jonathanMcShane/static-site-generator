import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode("p", "Test 1", None, {'href': 'www.google.com'})
        node2 = HTMLNode("p", "Test 1", None, {'href': 'www.google.com'})
        printed_node = node.props_to_html()
        printed_node2 = node2.props_to_html()

        self.assertEqual(printed_node, printed_node2)

class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        node = LeafNode("a", "Click me!", {"href": 'www.google.com', "target": '_blank'})
        html_node = node.to_html()
        self.assertEqual(
            html_node,
            '<a href="www.google.com" target="_blank">Click me!</a>'
        )

class TestParentNode(unittest.TestCase):

    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        print(node.to_html())


if __name__ == "__main__":
    unittest.main()
