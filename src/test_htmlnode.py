import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_props(self):
        grandchild_node = LeafNode("b", "grandchild", {"claSS": "bold"})
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node], {"id": "c1"})
        self.assertEqual(
            parent_node.to_html(),
            '<div id="c1"><span><b class="bold">grandchild</b></span></div>',
        )


if __name__ == "__main__":
    unittest.main()
