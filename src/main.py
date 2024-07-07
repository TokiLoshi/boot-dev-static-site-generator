from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
import os, shutil
from blocks import markdown_to_html_node

def extract_title(markdown):
  print(f"In the extract function")
  lines = markdown.split("\n")
  for line in lines:
    if line.startswith("# "):
      title = line[2:]
      return title
    raise ValueError("No title found")
  

def generate_page(from_path, template_path, dest_path):
  print(f"Generating path from {from_path} to {dest_path}")

  with open(from_path, "r") as from_file:
    from_text = from_file.read()

  print("From text read")

  with open(template_path, "r") as template_file:
    template_text = template_file.read()

  print("Template text read")
  
  from_count = 0
  for line in from_text.split("\n"):
    from_count += 1 
    # print(f"From line {from_count}: {line}")
  template_count = 0
  for line in template_text.split("\n"):
    template_count += 1
    # print(f"Template line {template_count}: {line}")

  print("Converting from markdown to html")
  # Convert markdown to HTML
  html_node = markdown_to_html_node(from_text)
  text_to_html = html_node.to_html()
  print(f"Converted successfully: {text_to_html}")

  # Extract title
  print("Extracting title")
  title = extract_title(from_text)
  print(f"Title extracted: {title}")

  # Replace placeholders
  template_text = template_text.replace("{{ Title }}", title)
  print(f"Replaced title: {template_text}")
  template_text = template_text.replace("{{ Content }}", text_to_html)
  print(f"Replaced content {template_text}")

  os.makedirs(os.path.dirname(dest_path), exist_ok=True)
  
  with open(dest_path, "w") as dest_file:
    dest_file.write(template_text)
  print(f"Generated page at {dest_path}")

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



def main():
  origin = "static"
  destination = "public"
  result = copy_static_files(origin, destination)
  generate_page("content/index.md", "template.html", "public/index.html")
  print("Changing directory to public and starting server")



main()
