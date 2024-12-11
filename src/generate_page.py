import os
from textnode import TextNode
from parentnode import ParentNode
from leafnode import LeafNode
from markdown_to_HTML_node import markdown_to_html_node
from extract_title import extract_title
import shutil

def reset_public():
    shutil.rmtree("/home/rboot/site_gen/public")
    os.makedirs("/home/rboot/site_gen/public")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path, 'r') as file:
        from_contents = file.read()
    with open(template_path, 'r') as file:
        template_contents = file.read()
    page_node = markdown_to_html_node(from_contents)
    page_string = page_node.to_html()
    title = extract_title(from_contents)
    added_title = template_contents.replace("{{ Title }}", title)
    added_contents = added_title.replace("{{ Content }}", page_string)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as file:
        file.write(added_contents)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    contents = os.listdir(dir_path_content)
    for item in contents:
        full_path = os.path.join(dir_path_content, item)
        if os.path.isfile(full_path):
            destination_path = os.path.join(dest_dir_path, item)
            if full_path.endswith(".md"):
                new_path = destination_path.replace(".md", ".html")
                generate_page(full_path, template_path, new_path)
            else:
                shutil.copy(full_path, destination_path)
        else:
            new_directory = os.path.join(dest_dir_path, item)
            os.mkdir(new_directory)
            generate_pages_recursive(full_path, template_path, new_directory)

