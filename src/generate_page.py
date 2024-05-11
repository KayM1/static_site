import os

from markdown_blocks import markdown_to_html_node
from markdown_blocks import extract_title
from htmlnode import LeafNode, ParentNode

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(f'{template_path}/template.html', 'r') as template_file:
        template_content = template_file.read()

    with open(f'{from_path}/markdown.md', 'r') as markdown_file:
        markdown_content = markdown_file.read()
        title = extract_title(markdown_content)
    
    html_content = markdown_to_html_node(markdown_content)

    html_content = template_content.replace("{{ Title }}", title)
    html_content = html_content.replace("{{ Content }}", html_content)

    with open(dest_path, 'w') as output_file:
        output_file.write(html_content)
    