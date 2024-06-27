import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_repr(self):
        node_obj = TextNode("The text", "italic", "link.com")
        expected_repr = 'TextNode(The text, italic, link.com)'

        self.assertEqual(repr(node_obj), expected_repr)


if __name__ == "__main__":
    unittest.main()