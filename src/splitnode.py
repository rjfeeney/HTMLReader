from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []
	for old_node in old_nodes:
		if old_node.text_type != TextType.TEXT:
			new_nodes.append(old_node)
		else:
			parts = old_node.value.split(delimiter)
			for index, part in enumerate(parts):
				if index % 2 == 0:
					new_nodes.append(TextNode(part, TextType.TEXT))
				else:
					if not part:
						raise ValueError(f"{delimiter} not found")
					else:
						new_nodes.append(TextNode(part, text_type))
	return new_nodes
