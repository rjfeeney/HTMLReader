import unittest
from textnode import TextNode, TextType
from leafnode import LeafNode
from text_to_html import to_html

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)

	def test_url_none(self):
		node = TextNode("This is a text node", TextType.ITALIC, None)
		node2 = TextNode("This is a text node",TextType.ITALIC, None)
		self.assertEqual(node, node2)

	def test_type_uneq(self):
		node = TextNode("This is a text node", TextType.TEXT)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertNotEqual(node, node2)

	def test_one_url(self):
		node = TextNode("This is a text node", TextType.BOLD, "https://www.youtube.com")
		node2 = TextNode("This is a text node", TextType.BOLD, None)
		self.assertNotEqual(node, node2)

##TEXTNODE -> HTML TESTS##
class TestTextToHTML(unittest.TestCase):
	def test_text_to_html(self):
		node = TextNode("This is a text node", TextType.TEXT)
		self.assertEqual(to_html(node), LeafNode(None, "This is a text node", None))

	def test_bold_to_html(self):
		node = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(to_html(node), LeafNode("b", "This is a text node", None))

	def test_italic_to_html(self):
		node = TextNode("This is a text node", TextType.ITALIC)
		self.assertEqual(to_html(node), LeafNode("i", "This is a text node", None))

	def test_code_to_html(self):
		node = TextNode("This is a text node", TextType.CODE)
		self.assertEqual(to_html(node), LeafNode("code", "This is a text node", None))

	def test_link_to_html(self):
		node = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
		self.assertEqual(to_html(node), LeafNode("a", "This is a text node", {"href": "https://www.google.com"}))

	def test_image_to_html(self):
		node = TextNode("This is a text node", TextType.IMAGE, "https://www.google.com")
		self.assertEqual(to_html(node), LeafNode("img", None, {"src": "https://www.google.com", "alt": "This is a text node"}))

if __name__ == "__main__":
	unittest.main()
