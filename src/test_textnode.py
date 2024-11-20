import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD_TEXT)
		node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
		self.assertEqual(node, node2)

	def test_url_none(self):
		node = TextNode("This is a text node", TextType.ITALIC_TEXT, None)
		node2 = TextNode("This is a text node",TextType.ITALIC_TEXT, None)
		self.assertEqual(node, node2)

	def test_type_uneq(self):
		node = TextNode("This is a text node", TextType.NORMAL_TEXT)
		node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
		self.assertNotEqual(node, node2)

	def test_one_url(self):
		node = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.youtube.com")
		node2 = TextNode("This is a text node", TextType.BOLD_TEXT, None)
		self.assertNotEqual(node, node2)




if __name__ == "__main__":
	unittest.main()
