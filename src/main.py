from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
import os, shutil
from blocks import markdown_to_html_node
from pathlib import Path
from generate_content import generate_pages_recursive, copy_static_files

static_dir_path = "./static"
public_dir_path = "./public"
content_dir_path = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(public_dir_path):
        shutil.rmtree(public_dir_path)

    print(f"Copying {static_dir_path} to {public_dir_path}...")
    copy_static_files(static_dir_path, public_dir_path)

    print("Generating html pages.")
    generate_pages_recursive(content_dir_path, template_path, public_dir_path)
    print("All done. Changing directory to public and starting server")



main()
