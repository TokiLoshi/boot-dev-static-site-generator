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
    print(f"Node: {old_node}")
    if old_node.text_type != text_type_text:
      new_nodes_list.append(old_node)
      print("About to continue", new_nodes_list)
      continue
    split_nodes = []
    sections = old_node.text.split(delimiter)
    print("Sections: ", sections)
    if len(sections) % 2 == 0:
      raise ValueError("That's invalid Markdown syntax, please add the correct closing delimiter")
    for i in range(len(sections)):
      print("segment: ", sections[i])
      if sections[i] == "":
        continue
      if i % 2 == 0:
        split_nodes.append(TextNode(sections[i], text_type_text))
      else:
        split_nodes.append(TextNode(sections[i], text_type))
    new_nodes_list.extend(split_nodes)
  return new_nodes_list


# def main():
#   text_type_text = "text"
#   text_type_code = "code"
#   node = TextNode("This is text with a `code block` word", text_type_text)
#   new_nodes = split_nodes_delimiter([node], "`", text_type_code)
#   for node in new_nodes:
#     print(node)

    
# if __name__ == "__main__":
#   main()