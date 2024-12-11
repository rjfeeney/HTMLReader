from textnode import TextNode, TextType
from splitnode import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnode(text):
    new_textnodes = [TextNode(text, TextType.TEXT)]
    for i, node in enumerate(new_textnodes):
        if new_textnodes[i].text_type == TextType.TEXT:
            nodes = split_nodes_delimiter([new_textnodes[i]], "**", TextType.BOLD)
            new_textnodes[i:i+1] = nodes
    for i, node in enumerate(new_textnodes):
        if node.text_type == TextType.TEXT:
            nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
            new_textnodes[i:i+1] = nodes
    for i, node in enumerate(new_textnodes):
        if node.text_type == TextType.TEXT:
            nodes = split_nodes_delimiter([node], "`", TextType.CODE)
            new_textnodes[i:i+1] = nodes            
    for i, node in enumerate(new_textnodes):
        if node.text_type == TextType.TEXT:
            nodes = split_nodes_link(node)
            new_textnodes[i:i+1] = nodes        
    for i, node in enumerate(new_textnodes):
        if node.text_type == TextType.TEXT:
            nodes = split_nodes_image(node)
            new_textnodes[i:i+1] = nodes
    return new_textnodes