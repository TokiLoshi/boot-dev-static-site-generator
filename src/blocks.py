from htmlnode import LeafNode, ParentNode

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

# def markdown_to_blocks(markdown):
#   blocks = [] 
#   current_block = []
#   lines = markdown.split("\n")
#   for line in lines: 
#     stripped_line = line.strip()
#     if stripped_line == "":
#       if current_block:
#         blocks.append(current_block)
#         current_block = []
#     else:
#       current_block.append(stripped_line)

#   if current_block:
#     blocks.append(current_block)
#   return blocks
def markdown_to_blocks(markdown):
  blocks = markdown.split("\n\n")
  filtered_blocks = []
  for block in blocks:
    if block.strip():
      filtered_blocks.append(block.strip())
  return filtered_blocks

def block_to_block_type(block):
    # Headings start with 1-6 # characters, followed by a space and then the heading text.
    block_lines = block.split("\n")
    if (block.startswith("# ") 
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")):
        return block_type_heading

    if block.startswith("```") and block[:3] == "```":
      return block_type_code

    if block.startswith("> "):
      for line in block_lines:
        if not line.startswith("> "):
          return block_type_paragraph
      return block_type_quote

    if block.startswith("*"):
      for line in block_lines: 
        if not line.startswith("*"):
          return block_type_paragraph
      return block_type_quote
    
    if block.startswith("1. "):
      count = 1
      for line in block_lines:
        if not line.startswith(f"{count}. "):
          return block_type_paragraph
        count += 1
        return block_type_ordered_list

    if block.startswith("- "):
      for line in block_lines:
        if not line.startswith("- "):
          return block_type_paragraph
      return block_type_unordered_list 

    return block_type_paragraph

def heading_markdown_block_to_html_node(block, type):
  count = 0
  for i in range(len(block)):
    if block[i] == "#":
      count += 1
    else:
      continue 
  tag = f"h{count}"
  text = block[count+1:].strip()
  new_node = LeafNode(tag, text, type)
  return new_node

def quote_markdown_block_to_html_node(block, type):
  new_node = LeafNode("blockquote", block[2:], type)
  return new_node

def code_markdown_block_to_html_node(block, type):
  if block.startswith("```") and block.endswith("```"):
    content = block[3:-3]
  else:
    content = block.strip()
  childNode = LeafNode("code", content, type)
  parentNode = ParentNode("pre", [childNode])
  return parentNode

def unordered_list_markdown_to_html_node(block, type):
  children = []
  for line in block: 
    if line.startswith("- "):
      childrenappend(LeafNode("li", line[2:], type))
  unordered_list = ParentNode("ul", children)
  return unordered_list

def ordered_list_markdown_to_html_node(block, type):
  children = []
  count = 1
  for line in block:
    if line.startswith(f"{count}. "):
      children.append(LeafNode("li", line[3:], type))
  ordered_list = ParentNode("ol", children)
  return ordered_list

def paragraph_markdown_to_html_node(block, type):
  new_node = LeafNode("p", block, type)
  return new_node

def markdown_to_html_node(markdown):
  # each child should be a block element 
  children = []
  
  # split markdown into blocks
  blocks = markdown_to_blocks(markdown)
  # iterate through the block 
  for block in blocks:
    # check the block type 
    block_type = block_to_block_type(block)
    # convert the block into html node
    if block_type == "heading":
      children.append(heading_markdown_block_to_html_node(block, block_type))
    elif block_type == "quote":
      children.append(quote_markdown_block_to_html_node(block, block_type))
    elif block_type == "code":
      children.append(code_markdown_block_to_html_node(block, block_type))
    elif block_type == "unordered_list":
      children.append(unordered_list_markdown_to_html_node(block, block_type))
    elif block_type == "ordered_list":
      children.append(ordered_list_markdown_to_html_node(block, block_type))
    elif block_type == "paragraph":
      children.append(paragraph_markdown_to_html_node(block, block_type))
    else:
      raise ValueError(f"Invalid block block_type")
  
    wrapper = ParentNode("div", children)
  return wrapper



def main():
  code = "- unordered_list list"
  check_type = block_to_block_type(code)
  print(f"Check type: {code}")
  if check_type == "unordered_list":
    result = unordered_list_markdown_to_html_node(code, check_type)
    print("result: ", result)


if __name__ == "__main__":
  main()
