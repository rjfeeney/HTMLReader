from textnode import TextNode, TextType
from leafnode import LeafNode

def to_html(node: TextNode):
		match node.text_type:

			case TextType.TEXT:
				result = LeafNode(None, node.text, None)
				return result

			case TextType.BOLD:
				result = LeafNode("b", node.text, None)
				return result

			case TextType.ITALIC:
				result = LeafNode("i", node.text, None)
				return result

			case TextType.CODE:
				result = LeafNode("code", node.text, None)
				return result

			case TextType.LINK:
				result = LeafNode("a", node.text, {"href": node.url})
				return result

			case TextType.IMAGE:
				result = LeafNode("img", None, {"src": node.url, "alt": node.text})
				return result

			case _:
				raise Exception("Invalid Text Type")