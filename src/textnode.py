from enum import Enum
from leafnode import LeafNode
class TextType(Enum):
	TEXT = "normal"
	BOLD = "bold"
	ITALIC = "italic"
	CODE = "code"
	LINK = "link"
	IMAGE = "image"

class TextNode:
	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, other):
		return self.text == other.text and self.text_type == other.text_type and self.url == other.url

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

	def text_node_to_html(self):
		match self.text_type:

			case TextType.TEXT:
				result = LeafNode(None, self.text, None)
				return result

			case TextType.BOLD:
				result = LeafNode("b", self.text, None)
				return result

			case TextType.ITALIC:
				result = LeafNode("i", self.text, None)
				return result

			case TextType.CODE:
				result = LeafNode("code", self.text, None)
				return result

			case TextType.LINK:
				result = LeafNode("a", self.text, {"href": self.url})
				return result

			case TextType.IMAGE:
				result = LeafNode("img", None, {"src": self.url, "alt": self.text})
				return result

			case _:
				raise Exception("Invalid Text Type")
