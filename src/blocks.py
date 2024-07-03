block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
  blocks = [] 
  current_block = []
  lines = markdown.split("\n")
  for line in lines: 
    stripped_line = line.strip()
    if stripped_line == "":
      if current_block:
        blocks.append(current_block)
        current_block = []
    else:
      current_block.append(stripped_line)

  if current_block:
    blocks.append(current_block)
  return blocks

# def main():
#   markdown = """
#   # This is **bolded** paragraph

# This is another paragraph with *italic* text and `code` here
# This is the same paragraph on a new line

# * This is a list
# * with items
#   """
#   blocks = markdown_to_blocks(markdown)
#   print(blocks)
#   # for block in blocks:
#   #   print(block)

# if __name__ == "__main__":
#   main()

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
  
  # Unordered list
  # must start with * or - and be followed by a space 
  # if block.startswith("* "): 
  #   list_type = "*"
  #   for i in range(len(block)):
  #     if block[i] == "\n":
  #       if block[i+1] != "* ":
  #         raise ValueError("Invalid unordered list")
  #   return block_type_unordered_list
  # if block.startswith("- "):
  #   for i in range(len(block)):
  #     if block[i] == "\n":
  #       if block[i+1] != "= ":
  #         raise ValueError("Invalid unordered list")
  #   return block_type_unordered_list

  # Paragraph
  # if none of the above conditions are met it's a normal paragraph 
  # return block_type_paragraph

def main():
  ul = "- invalid list"
  ul2 = "- startlist \n- foo"
  ptag = "This is a valid paragraph"


  test17 = block_to_block_type(ul)
  test19 = block_to_block_type(ul2)
  test20 = block_to_block_type(ptag)
  print("Lets test this stuff")
  print(f"Test: {test20}")


if __name__ == "__main__":
  main()
