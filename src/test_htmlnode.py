import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
