import unittest

from markdown_to_blocks import markdown_to_blocks

class test_markdown_to_blocks(unittest.TestCase):
    def test_empty_string(self):
        markdown = ""
        self.assertEqual(markdown_to_blocks(markdown), [])

    def test_integer(self):
        with self.assertRaises(TypeError):
             markdown_to_blocks(3)
        
    def test_two_splits(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        self.assertEqual(markdown_to_blocks(markdown), [
        "# This is a heading",
        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
        "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
    ])


    def test_leading_trailing_space(self):
        markdown = """
         
         
        # This is a heading

         
         
This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item



"""
        self.assertEqual(markdown_to_blocks(markdown), [
        "# This is a heading",
        "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
        "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
    ])


if __name__ == '__main__':
	unittest.main()