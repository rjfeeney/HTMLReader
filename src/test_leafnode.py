import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

	def test1(self):
		node = LeafNode(None, "This is test text", None)
		self.assertEqual(node.to_html(), "This is test text")

	def test2(self):
		with self.assertRaises(ValueError):
			node = LeafNode("p", None, {"height": "700"})
			node.to_html()

	def test3(self):
		node = LeafNode("p", "This is test text", None)
		self.assertEqual(node.to_html(), "<p>This is test text</p>")

	def test4(self):
		node = LeafNode(None, "This is test text", {"height": "700"})
		self.assertEqual(node.to_html(), "This is test text")

	def test5(self):
		node = LeafNode("p", "This is test text", {"height": "700"})
		self.assertEqual(node.to_html(), '<p height="700">This is test text</p>')
