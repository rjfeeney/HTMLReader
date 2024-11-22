import unittest
from extractmarkdown import *

class TestExtractMarkdown(unittest.TestCase):
	def test_one_image(self):
		text = "Here is one ![image](img.jpg)"
		self.assertEqual(extract_markdown_images(text), [("image", "img.jpg")])

	def test_two_images(self):
		text = "Here is one ![image1](img1.jpg) and another ![image2](img2.jpg)"
		self.assertEqual(extract_markdown_images(text), [("image1", "img1.jpg"), ("image2", "img2.jpg")])

	def test_one_link(self):
		text = "Here is text with one link [Link](https://www.google.com)"
		self.assertEqual(extract_markdown_links(text), [("Link", "https://www.google.com")])

	def test_two_links(self):
		text = "Here is text with one link [Link1](https://www.google.com) and another link [Link2](https://www.youtube.com)"
		self.assertEqual(extract_markdown_links(text), [("Link1", "https://www.google.com"), ("Link2", "https://www.youtube.com")])

	def test_image_and_link(self):
		text = "Here is text with one ![image](img.jpg) and one link [Link](https://www.google.com)"
		self.assertEqual(extract_markdown_images(text), [("image", "img.jpg")])
		self.assertEqual(extract_markdown_links(text), [("Link", "https://www.google.com")])

	def test_images_and_links(self):
		text = "Here is text with one ![image1](img1.jpg), one link [Link1](https://www.google.com), another ![image2](img2.jpg), and another link [Link2](https://www.youtube.com)"
		self.assertEqual(extract_markdown_images(text), [("image1", "img1.jpg"), ("image2", "img2.jpg")])
		self.assertEqual(extract_markdown_links(text), [("Link1", "https://www.google.com"), ("Link2", "https://www.youtube.com")])

	def test_empty(self):
		text = ""
		self.assertEqual(extract_markdown_links(text), [])
		self.assertEqual(extract_markdown_images(text), [])

	def test_plain_text(self):
		text = "This is plain text"
		self.assertEqual(extract_markdown_links(text), [])
		self.assertEqual(extract_markdown_images(text), [])


if __name__ == "__main__":
	unittest.main()
