import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []
	if not isinstance(old_nodes, list):
		old_nodes = [old_nodes]
	for old_node in old_nodes:
		if old_node.text_type != TextType.TEXT:
			new_nodes.append(old_node)
		else:
			parts = old_node.text.split(delimiter)
			for index, part in enumerate(parts):
				if index % 2 == 0:
					new_nodes.append(TextNode(part, TextType.TEXT))
				else:
					if not part:
						raise ValueError(f"{delimiter} not found")
					else:
						new_nodes.append(TextNode(part, text_type))
	return new_nodes

node = TextNode("Hello **world**", TextType.TEXT)
result = split_nodes_delimiter(node, "**", TextType.BOLD)
print(result)

def split_nodes_link(old_nodes):
	if not isinstance(old_nodes, list):
		old_nodes = [old_nodes]
	new_nodes = []
	pattern = r"(?<!!)[\[]"
	for old_node in old_nodes:
		if old_node.text == "":
			continue
		elif not re.search(pattern, old_node.text):
			new_nodes.append(old_node)
		else:
			remaining_text = old_node.text
			while remaining_text:
				first_split = re.split(pattern, remaining_text, 1)
				new_nodes.append(TextNode(first_split[0], TextType.TEXT))
				if len(first_split) > 1:
					second_split = first_split[1].split("]", 1)
					alt_text = second_split[0]
					if len(second_split) > 1:
						remaining_link = second_split[1]
						third_split = remaining_link.split("(", 1)
						if len(third_split) > 1:
							link_and_rest = third_split[1].split(")", 1)
							url = link_and_rest[0]
							new_nodes.append(TextNode(alt_text, TextType.LINK, url))
							if len(link_and_rest) > 1:
								remaining_text = link_and_rest[1]
							else:
								remaining_text = ""
						else:
							remaining_text = ""
					else:
						remaining_text = ""
				else:
					remaining_text = ""
	return new_nodes



def split_nodes_image(old_nodes):
	new_nodes = []
	if not isinstance(old_nodes, list):
		old_nodes = [old_nodes]
	for old_node in old_nodes:
		if old_node.text == "":
			continue
		elif '![' not in old_node.text:
			new_nodes.append(old_node)
		else:
			remaining_text = old_node.text
			while remaining_text:
				first_split = remaining_text.split("![", 1)
				new_nodes.append(TextNode(first_split[0], TextType.TEXT))
				if len(first_split) > 1:
					second_split = first_split[1].split("]", 1)
					alt_text = second_split[0]
					if len(second_split) > 1:
						remaining_link = second_split[1]
						third_split = remaining_link.split("(", 1)
						if len(third_split) > 1:
							link_and_rest = third_split[1].split(")", 1)
							url = link_and_rest[0]
							new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
							if len(link_and_rest) > 1:
								remaining_text = link_and_rest[1]
							else:
								remaining_text = ""
						else:
							remaining_text = ""
					else:
						remaining_text = ""
				else:
					remaining_text = ""
	return new_nodes
