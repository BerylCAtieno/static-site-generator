import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        
        # Test case with sample properties
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(props=props)
        expected_output = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_output)

        # Test case with no properties
        props = {}
        node = HTMLNode(props=props)
        expected_output = ''
        self.assertEqual(node.props_to_html(), expected_output)

        # Test case with one property
        props = {"class": "btn"}
        node = HTMLNode(props=props)
        expected_output = 'class="btn"'
        self.assertEqual(node.props_to_html(), expected_output)

        # Test case with multiple properties
        props = {"id": "main", "style": "color: red;"}
        node = HTMLNode(props=props)
        expected_output = 'id="main" style="color: red;"'
        self.assertEqual(node.props_to_html(), expected_output)

class TestLeafNode(unittest.TestCase):

    def test_to_html_with_tag_and_props(self):
        # Test case with tag, value, and props
        node = LeafNode(tag='a', value='Click me!', props={"href": "https://www.google.com"})
        expected_output = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected_output)

    def test_to_html_with_tag_no_props(self):
        # Test case with tag and value but no props
        node = LeafNode(tag='p', value='This is a paragraph of text.')
        expected_output = '<p>This is a paragraph of text.</p>'
        self.assertEqual(node.to_html(), expected_output)

    def test_to_html_with_no_tag(self):
        # Test case with no tag, should return raw text
        node = LeafNode(tag=None, value='Just some text.')
        expected_output = 'Just some text.'
        self.assertEqual(node.to_html(), expected_output)

    def test_to_html_with_no_value(self):
        # Test case with no value, should raise ValueError
        node = LeafNode(tag='p', value=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_tag_empty_props(self):
        # Test case with tag, value, and empty props
        node = LeafNode(tag='div', value='Content', props={})
        expected_output = '<div>Content</div>'
        self.assertEqual(node.to_html(), expected_output)

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_valid_children(self):
        # Test case with valid children
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected_output = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(node.to_html(), expected_output)

    def test_to_html_with_no_tag(self):
        # Test case with no tag
        with self.assertRaises(ValueError) as context:
            ParentNode(
                None,
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                ]
            )
        self.assertEqual(str(context.exception), "ParentNode must have a tag")

    def test_to_html_with_no_children(self):
        # Test case with no children
        with self.assertRaises(ValueError) as context:
            ParentNode("p", [])
        self.assertEqual(str(context.exception), "ParentNode must have at least one child")

    def test_to_html_with_nested_parent_nodes(self):
        # Test case with nested ParentNode
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                    ],
                ),
                LeafNode("i", "italic text"),
            ],
        )
        expected_output = '<div><p><b>Bold text</b>Normal text</p><i>italic text</i></div>'
        self.assertEqual(node.to_html(), expected_output)

    def test_to_html_with_props(self):
        # Test case with properties
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
            ],
            props={"class": "text-class"}
        )
        expected_output = '<p class="text-class"><b>Bold text</b>Normal text</p>'
        self.assertEqual(node.to_html(), expected_output)

if __name__ == "__main__":
    unittest.main()