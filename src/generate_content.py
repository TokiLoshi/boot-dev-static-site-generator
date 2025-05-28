from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
import os, shutil
from blocks import markdown_to_html_node
from pathlib import Path

def extract_title(markdown):
  print(f"In the extract function")
  lines = markdown.split("\n")
  for line in lines:
    if line.startswith("# "):
      title = line[2:]
      return title
    raise ValueError("No title found")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
  # Ensure destination directory exists
  origin = dir_path_content
  destination = dest_dir_path
  filenames = os.listdir(dir_path_content)
  for file in filenames:
    from_path = os.path.join(origin, file)
    to_path = os.path.join(destination, file)
    if os.path.isfile(from_path):
      to_path = Path(to_path).with_suffix(".html")
      generate_page(from_path, template_path, to_path, base_path)
    else:
      generate_pages_recursive(from_path, template_path, to_path, base_path)


def generate_page(from_path, template_path, dest_path, base_path):
  print(f"Generating path from {from_path} to {dest_path}")

  from_file = open(from_path, "r")
  markdown_content = from_file.read()
  from_file.close()

  template_file = open(template_path, "r")
  template = template_file.read()
  template_file.close()

  print("From file and template file read, converting markdown to HTML")

  node = markdown_to_html_node(markdown_content)
  title = extract_title(markdown_content)
  html = node.to_html()

  # Update placeholders in template
  template = template.replace("{{ Title }}", title)
  template = template.replace("{{ Content }}", html)
  template = template.replace('href="/', 'src="{base_path}')
  template = template.replace('src="/', 'src="{base_path}')

  destination = os.path.dirname(dest_path)
  if destination != "":
    os.makedirs(destination, exist_ok=True)
  to_file = open(dest_path, "w")
  to_file.write(template) 
  to_file.close()


def copy_static_files(origin, destination):
  
  # If the path doesn't exist, create it
  if not os.path.exists(destination):
    print(f"Creating directory: {destination}")
    os.mkdir(destination)
  
  # check for an invalid folder name
  if not os.path.exists(origin):
    raise NameError("Invalid folder")

  files = os.listdir(origin)
  for file in files:
    path = os.path.join(origin, file)
    new_destination_path = os.path.join(destination, file)
    print(f"Copy {path} to {new_destination_path}")
    
    if os.path.isfile(path):
      print(f"We have a file {path}")
      shutil.copy(path, new_destination_path)
      print(f"Copied! {path}")
    
    else:
      print(f"This is not a file, {path}")
      if not os.path.exists(new_destination_path):
        os.mkdir(new_destination_path)
      copy_static_files(path, new_destination_path)
      
  print("Done copying files")