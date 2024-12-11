import unittest
from splitnode import split_nodes_delimiter, split_nodes_link, split_nodes_image
from textnode import TextNode, TextType

class TestImageAndLinkSplit(unittest.TestCase):
	def test_empty_string(self):
		node = TextNode("", TextType.TEXT)
		self.assertEqual(split_nodes_image([node]), [])
		self.assertEqual(split_nodes_link([node]), [])

	def test_normal_text(self):
		node = TextNode("Normal Text", TextType.TEXT)
		self.assertEqual(split_nodes_image([node]), [TextNode("Normal Text", TextType.TEXT)])
		self.assertEqual(split_nodes_link([node]), [TextNode("Normal Text", TextType.TEXT)])

	def test_one_image(self):
		node = TextNode("This text has an ![image](img.jpg) in it", TextType.TEXT)
		self.assertEqual(split_nodes_image([node]), [TextNode("This text has an ", TextType.TEXT), TextNode("image", TextType.IMAGE, "img.jpg"), TextNode(" in it", TextType.TEXT)])
		self.assertEqual(split_nodes_link([node]), [node])

	def test_two_images(self):
		node = TextNode("This text has one ![image1](img1.jpg) and another ![image2](img2.jpg) in it", TextType.TEXT)
		self.assertEqual(split_nodes_image([node]), [TextNode("This text has one ", TextType.TEXT), TextNode("image1", TextType.IMAGE, "img1.jpg"), TextNode(" and another ", TextType.TEXT), TextNode("image2", TextType.IMAGE, "img2.jpg"), TextNode(" in it", TextType.TEXT)])
		self.assertEqual(split_nodes_link([node]), [node])

	def test_one_link(self):
		node = TextNode("This text has one [Link](https://www.google.com) in it", TextType.TEXT)
		self.assertEqual(split_nodes_image([node]), [node])
		self.assertEqual(
		split_nodes_link([node]),
		[
			TextNode("This text has one ", TextType.TEXT),
			TextNode("Link", TextType.LINK, "https://www.google.com"),
			TextNode(" in it", TextType.TEXT)
			]
		)

	def test_two_links(self):
		node = TextNode("This text has one [Link1](https://www.google.com) and another [Link2](https://www.youtube.com) in it", TextType.TEXT)
		self.assertEqual(split_nodes_image([node]), [node])
		self.assertEqual(
		split_nodes_link([node]),
		[
			TextNode("This text has one ", TextType.TEXT),
			TextNode("Link1", TextType.LINK, "https://www.google.com"),
			TextNode(" and another ", TextType.TEXT),
			TextNode("Link2", TextType.LINK, "https://www.youtube.com"),
			TextNode(" in it", TextType.TEXT)
			]
		)

	def test_one_image_one_link(self):
		node = TextNode("This text has one ![image](img.jpg) and one [Link](https://www.google.com) in it", TextType.TEXT)
		self.assertEqual(
		split_nodes_image([node]),
		[
			TextNode("This text has one ", TextType.TEXT),
			TextNode("image", TextType.IMAGE, "img.jpg"),
			TextNode(" and one [Link](https://www.google.com) in it", TextType.TEXT)
			]
		)
		self.assertEqual(
		split_nodes_link([node]),
		[
			TextNode("This text has one ![image](img.jpg) and one ", TextType.TEXT),
			TextNode("Link", TextType.LINK, "https://www.google.com"),
			TextNode(" in it", TextType.TEXT)
			]
		)


	def test_two_images_two_links(self):
		node = TextNode("This text has one ![image1](img1.jpg) and one [Link1](https://www.google.com) and another ![image2](img2.jpg) and another [Link2](https://www.youtube.com) in it", TextType.TEXT)
		self.assertEqual(
		split_nodes_image([node]),
		[
			TextNode("This text has one ", TextType.TEXT),
			TextNode("image1", TextType.IMAGE, "img1.jpg"),
			TextNode(" and one [Link1](https://www.google.com) and another ", TextType.TEXT),
			TextNode("image2", TextType.IMAGE, "img2.jpg"),
			TextNode(" and another [Link2](https://www.youtube.com) in it", TextType.TEXT)
			]
		)
		self.assertEqual(
		split_nodes_link([node]),
		[
			TextNode("This text has one ![image1](img1.jpg) and one ", TextType.TEXT),
			TextNode("Link1", TextType.LINK, "https://www.google.com"),
			TextNode(" and another ![image2](img2.jpg) and another ", TextType.TEXT),
			TextNode("Link2", TextType.LINK, "https://www.youtube.com"),
			TextNode(" in it", TextType.TEXT)
			]
		)

if __name__ == "__main__":
	unittest.main()
