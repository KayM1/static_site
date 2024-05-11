import os
from markdown_blocks import markdown_to_html_node
from pathlib import Path


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    
    # Read Markdown content from file
    with open(from_path, "r") as from_file:
        markdown_content = from_file.read()

    # Read template content from file
    with open(template_path, "r") as template_file:
        template = template_file.read()

    # Generate HTML content from Markdown
    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    # Extract title from Markdown content
    title = extract_title(markdown_content)

    # Replace placeholders in the template with title and HTML content
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    # Create destination directory if it doesn't exist
    dest_dir_path = os.path.dirname(dest_path)
    os.makedirs(dest_dir_path, exist_ok=True)

    # Write HTML content to destination file
    with open(dest_path, "w") as to_file:
        to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)