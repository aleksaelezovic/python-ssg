import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        tag = "p"
        value = "some text"
        props = {"class": "color-yellow"}
        node = HTMLNode(tag, value, None, props)
        expected = f"HTMLNode({tag}, {value}, {None}, {props})"
        self.assertEqual(expected, f"{node}")

    def test_props(self):
        tag = "p"
        value = "some text"
        props = {"class": "color-yellow", "id": "p12"}
        node = HTMLNode(tag, value, None, props)
        expected = ' class="color-yellow" id="p12"'
        self.assertEqual(expected, node.props_to_html())

    def test_props_case_insensitive(self):
        tag = "p"
        value = "some text"
        props = {"cLAsS": "color-yellow", "ID": "p12"}
        node = HTMLNode(tag, value, None, props)
        expected = ' class="color-yellow" id="p12"'
        self.assertEqual(expected, node.props_to_html())


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual("<p>Hello, world!</p>", node.to_html())

    def test_leaf_to_html_with_props(self):
        props = {"CLass": "color-blue", "ID": "p4"}
        node = LeafNode("p", "Hello, world!", props)
        expected = '<p class="color-blue" id="p4">Hello, world!</p>'
        self.assertEqual(expected, node.to_html())

    def test_leaf_to_html_raw(self):
        node = LeafNode(None, "a text Node")
        self.assertEqual("a text Node", node.to_html())


if __name__ == "__main__":
    unittest.main()
