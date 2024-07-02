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

def main():
  markdown = """
  # This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
  """
  blocks = markdown_to_blocks(markdown)
  print(blocks)
  # for block in blocks:
  #   print(block)

if __name__ == "__main__":
  main()
