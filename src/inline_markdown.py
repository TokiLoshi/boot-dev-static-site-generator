import re

from textnode import (
  TextNode,
  text_type_text,
  text_type_bold,
  text_type_italic,
  text_type_code,
  text_type_link,
  text_type_image
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  delimiter_object = {
    "**" : "bold",
    "*" : "italic",
    "`" : "code",
    "[" : "link",
    "!" : "image"
    }
  if delimiter not in delimiter_object:
    raise ValueError("Invalid delimiter")
  
  new_nodes_list = []
  for old_node in old_nodes:
    if old_node.text_type != text_type_text:
      new_nodes_list.append(old_node)
      continue
    split_nodes = []
    sections = old_node.text.split(delimiter)
    if len(sections) % 2 == 0:
      raise ValueError("That's invalid Markdown syntax, please add the correct closing delimiter")
    for i in range(len(sections)):
      if sections[i] == "":
        continue
      if i % 2 == 0:
        split_nodes.append(TextNode(sections[i], text_type_text))
      else:
        split_nodes.append(TextNode(sections[i], text_type))
    new_nodes_list.extend(split_nodes)
  return new_nodes_list


def extract_markdown_images(text):
  parse_text = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
  return parse_text

def extract_markdown_links(text):
  parse_text = re.findall(r"\[(.*?)\]\((.*?)\)", text)
  return parse_text

def split_nodes_images(old_nodes):
  new_nodes_list = [] 
  for old_node in old_nodes:
    if old_node.text_type != text_type_text:
      new_nodes_list.append(old_node) 
      continue
    original_text = old_node.text
    images = extract_markdown_images(original_text)
    if len(images) == 0:
      new_nodes_list.append(old_node)
      continue
    for image in images:
      sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
      if len(sections) != 2:
        raise ValueError("Invalid Markdown syntax, image section not closed")
      if sections[0] != "":
        new_nodes_list.append(TextNode(sections[0], text_type_text))
        new_nodes_list.append(TextNode(image[0], text_type_image, image[1]))
      original_text = sections[1]
      if original_text != "":
        new_nodes_list.append(TextNode(original_text, text_type_text))
  return new_nodes_list

def split_nodes_link(old_nodes):
  new_nodes_list = []
  for old_node in old_nodes:
    if old_node.text_type != text_type_text:
      new_nodes_list.append(old_node)
      continue
    original_text = old_node.text
    links = extract_markdown_links(original_text)
    if len(links) == 0:
      new_nodes_list.append(old_node)
      continue
    for link in links:
      sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
      if len(sections) != 2:
        raise ValueError("Invalid Markdown syntax, link section not closed")
      if sections[0] != "":
        new_nodes_list.append(TextNode(sections[0], text_type_text))
      new_nodes_list.append(TextNode(link[0], text_type_link, link[1]))
      original_text = sections[1]
      if original_text != "":
        new_nodes_list.append(TextNode(original_text, text_type_text))
  return new_nodes_list     # if it's text then we want to append each part that's text 


def text_to_textnodes(text):
  nodes = [TextNode(text, text_type_text)]
  nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
  nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
  nodes = split_nodes_delimiter(nodes, "`", text_type_code)
  nodes = split_nodes_images(nodes)
  nodes = split_nodes_link(nodes)
  return nodes

def main():
#   text_type_text = "text"
#   text_type_code = "code"
#   node = TextNode("This is text with a `code block` word", text_type_text)
#   new_nodes = split_nodes_delimiter([node], "`", text_type_code)
#   for node in new_nodes:
#     print(node)
  text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
  # matches = re.findall(r"\w+@\w+\.\w+", text)
  matches = extract_markdown_images(text)
  # print(f"MATHCES: {matches}") # ['lane@example.com', 'hunter@example.com']
  text2 = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
  # print(extract_markdown_links(text))
  # [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]

    
if __name__ == "__main__":
  main()