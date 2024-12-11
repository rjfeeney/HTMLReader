from enum import Enum
from htmlnode import HTMLNode
class TextType(Enum):
	TEXT = "normal"
	BOLD = "bold"
	ITALIC = "italic"
	CODE = "code"
	LINK = "link"
	IMAGE = "image"

class TextNode(HTMLNode):
	def __init__(self, text, text_type, url=None):
		super().__init__()
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, other):
		return self.text == other.text and self.text_type == other.text_type and self.url == other.url

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
	
	def to_html(self):
		match self.text_type:

			case TextType.TEXT:
				return self.text

			case TextType.BOLD:
				return f"<b>{self.text}</b>"

			case TextType.ITALIC:
				return f"<i>{self.text}</i>"

			case TextType.CODE:
				return f"<code>{self.text}</code>"

			case TextType.LINK:
				return f"<a href='{self.url}'>{self.text}</a>"

			case TextType.IMAGE:
				return f"<img src='{self.url}' alt='{self.text}'>"

			case _:
				raise Exception("Invalid Text Type")
