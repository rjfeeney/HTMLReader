from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from text_to_textnode import text_to_textnode
from text_to_html import to_html
from parentnode import ParentNode
from leafnode import LeafNode


def text_to_children(removed_text):
    child_nodes = []
    text_nodes = text_to_textnode(removed_text)
    for text_node in text_nodes:
        html_node = to_html(text_node)
        child_nodes.append(html_node)
    return child_nodes

def markdown_to_html_node(markdown):
    parent = ParentNode(tag="div", children=[])
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == "Heading":
            tag_count = 0
            for char in block:
                if char == "#":
                    tag_count += 1
            removed_text = block[tag_count + 1:].strip()
            heading_tag = f"h{tag_count}"
            html_nodes = text_to_children(removed_text)
            heading_node = ParentNode(tag=heading_tag, children=html_nodes)
            parent.children.append(heading_node)
        elif block_type == "Code":
            text = block.strip('`').strip()
            code_node = LeafNode(tag="code", value=text)
            pre_node = ParentNode(tag="pre", children=[code_node])
            parent.children.append(pre_node)
        elif block_type == "Quote":
            text = block[block.find(">") + 1:].strip()
            html_nodes = text_to_children(text)
            quote_node = ParentNode(tag="blockquote", children=html_nodes)
            parent.children.append(quote_node)
        elif block_type == "Unordered List":
            li_nodes = []
            split_lines = block.split("\n")
            for split_line in split_lines:
                line_without_marker = split_line.lstrip("* ")
                html_nodes = text_to_children(line_without_marker)
                li_nodes.append(ParentNode(tag="li", children=html_nodes))
            ul_node = ParentNode(tag="ul", children=li_nodes)
            parent.children.append(ul_node)
        elif block_type == "Ordered List":
            li_nodes = []
            split_lines = block.split("\n")
            for split_line in split_lines:
                parts = split_line.split(". ", 1)
                line_without_marker = parts[1]
                if "[ ]" in line_without_marker:
                    removed_bracket = line_without_marker.split("[ ]", 1)[1]
                    html_nodes = text_to_children(removed_bracket)
                else:
                    html_nodes = text_to_children(line_without_marker)
                li_nodes.append(ParentNode(tag="li", children=html_nodes))
            ol_node = ParentNode(tag="ol", children=li_nodes)
            parent.children.append(ol_node)
        elif block_type == "Paragraph":
            if block.strip():
                paragraph_nodes = text_to_children(block)
                p_tag_node = ParentNode(tag="p", children=paragraph_nodes)
                parent.children.append(p_tag_node)  
    return parent