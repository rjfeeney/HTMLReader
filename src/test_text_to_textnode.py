import unittest

from textnode import TextNode, TextType
from text_to_textnode import text_to_textnode
from splitnode import split_nodes_delimiter, split_nodes_image, split_nodes_link

class Test_Text_To_TextNode(unittest.TestCase):
    def test_empty(self):
        text = ""
        self.assertEqual(text_to_textnode(text), [])

    def test_all_normal(self):
        text = "This is all normal text."
        self.assertEqual(text_to_textnode(text), [TextNode("This is all normal text.", TextType.TEXT)])


    def test_one_of_each(self):
        text = "This is **bold** text, *italicized* text, a `code` block, a [Link](https://www.google.com) and an ![image](img.jpg)"
        self.assertEqual(
        text_to_textnode(text), 
        [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text, ", TextType.TEXT),
            TextNode("italicized", TextType.ITALIC),
            TextNode(" text, a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" block, a ", TextType.TEXT),
            TextNode("Link", TextType.LINK, "https://www.google.com"),
            TextNode(" and an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "img.jpg")
        ])


    def test_two_of_each(self):
        text = "**This** is **bold** text, *italicized* *text,* two `code` `blocks,` a [Link1](https://www.google.com) an ![image1](img1.jpg) another [Link2](https://www.youtube.com) and another ![image2](img2.jpg)"
        self.assertEqual(
        text_to_textnode(text), 
        [
            TextNode("This", TextType.BOLD),
            TextNode(" is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text, ", TextType.TEXT),
            TextNode("italicized", TextType.ITALIC),
            TextNode(" ", TextType.TEXT),
            TextNode("text,", TextType.ITALIC),
            TextNode(" two ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("blocks,", TextType.CODE),
            TextNode(" a ", TextType.TEXT),
            TextNode("Link1", TextType.LINK, "https://www.google.com"),
            TextNode(" an ", TextType.TEXT),
            TextNode("image1", TextType.IMAGE, "img1.jpg"),
            TextNode(" another ", TextType.TEXT),
            TextNode("Link2", TextType.LINK, "https://www.youtube.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("image2", TextType.IMAGE, "img2.jpg")
        ])


    def test_1bold_1italic_0code_2link_0_image(self):
        text = "This is **bold** text, *italicized* text, no code blocks, a [Link1](https://www.google.com) and another [Link2](https://www.youtube.com)"
        self.assertEqual(
        text_to_textnode(text), 
        [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text, ", TextType.TEXT),
            TextNode("italicized", TextType.ITALIC),
            TextNode(" text, no code blocks, a ", TextType.TEXT),
            TextNode("Link1", TextType.LINK, "https://www.google.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("Link2", TextType.LINK, "https://www.youtube.com")
        ])


if __name__ == '__main__':
	unittest.main()