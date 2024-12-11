import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
	def test_children2_props0(self):
		child1 = LeafNode("b", "Bold text")
		child2 = LeafNode(None, "Normal text")
		node = ParentNode("p", [child1, child2], None)
		self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text</p>")

	def test_children1_props0(self):
		child1 = LeafNode("b", "Bold text")
		node = ParentNode("p", [child1], None)
		self.assertEqual(node.to_html(), "<p><b>Bold text</b></p>")

	def test_children2_props1(self):
		child1 = LeafNode("b", "Bold text")
		child2 = LeafNode(None, "Normal text")
		node = ParentNode("p", [child1, child2], {"height": "700"})
		self.assertEqual(node.to_html(), '<p height="700"><b>Bold text</b>Normal text</p>')


	def test_children3_props2(self):
		child1 = LeafNode("b", "Bold text")
		child2 = LeafNode("i", "Italicized text")
		child3 = LeafNode(None, "Normal text")
		node = ParentNode("p", [child1, child2, child3], {"height": "700", "width": "50"})
		self.assertEqual(node.to_html(), '<p height="700" width="50"><b>Bold text</b><i>Italicized text</i>Normal text</p>')

	def test_missing_tag_children2_props0(self):
		child1 = LeafNode("b", "Bold text")
		child2 = LeafNode("i", "Italicized text")
		with self.assertRaises(ValueError):
			node = ParentNode(None, [child1, child2], None)
			node.to_html()

	def test_children2_both_missing_tags(self):
		child1 = LeafNode(None, "Normal text")
		child2 = LeafNode(None, "Normal text two")
		node = ParentNode("p", [child1, child2], None)
		self.assertEqual(node.to_html(), "<p>Normal textNormal text two</p>")

	def test_children2_one_missing_tag(self):
		child1 = LeafNode(None, "Normal text")
		child2 = LeafNode("b", "Bold text")
		node = ParentNode("p", [child1, child2], None)
		self.assertEqual(node.to_html(), "<p>Normal text<b>Bold text</b></p>")

	def test_children2_two_missing_tag(self):
		child1 = LeafNode("b", "Bold text")
		child2 = LeafNode(None, "Normal text")
		node = ParentNode("p", [child1, child2], None)
		self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text</p>")

	def test_children1_missing_tag_props2(self):
		child1 = LeafNode(None, "Normal text")
		node = ParentNode("p", [child1], {"height": "700", "width": "50"})
		self.assertEqual(node.to_html(), '<p height="700" width="50">Normal text</p>')


if __name__ == '__main__':
	unittest.main()
