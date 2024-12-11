from extract_title import extract_title
import unittest

class TestExtractTitle(unittest.TestCase):
    def test_empty(self):
        with self.assertRaises(Exception):
            markdown = ""
            extract_title(markdown)
		
    def test_no_title(self):
        with self.assertRaises(Exception):
            markdown = "32jfkdksp# "
            extract_title(markdown)

    def test_title_first_line(self):
        markdown = "# Title\n\nsome text\n\nmore text"
        self.assertEqual(extract_title(markdown), "Title")

    def test_title_third_line_whitespace(self):
        markdown = "some text\n\nmore text\n\n#    Title    "            
        self.assertEqual(extract_title(markdown), "Title")

if __name__ == "__main__":
	unittest.main()