import unittest

from htmlnode import HTMLNode


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

if __name__ == '__main__':
    unittest.main()