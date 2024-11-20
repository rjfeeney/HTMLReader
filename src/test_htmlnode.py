import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test1(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test2(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test3(self):
        node = HTMLNode(None, None, None, None)
        self.assertEqual(node.props_to_html(), "")

    def test4(self):
        node = HTMLNode(None, None, None, {"length": 600})
        self.assertEqual(node.props_to_html(), ' length="600"')
