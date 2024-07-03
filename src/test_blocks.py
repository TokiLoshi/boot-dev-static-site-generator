import unittest
from blocks import markdown_to_blocks, block_to_block_type, block_type_heading, block_type_quote, block_type_code, block_type_ordered_list, block_type_unordered_list, block_type_paragraph

class TestMarkdownToBlocks(unittest.TestCase):
  def test_markdown_to_blocks(self):
    markdown = """
                # This is **bolded** paragraph

                This is another paragraph with *italic* text and `code` here
                This is the same paragraph on a new line

                * This is a list
                * with items
              """
    self.assertEqual([['# This is **bolded** paragraph'], ['This is another paragraph with *italic* text and `code` here', 'This is the same paragraph on a new line'], ['* This is a list', '* with items']], markdown_to_blocks(markdown))

class TestBlockToBlockType(unittest.TestCase):
  def test_block_to_block_type_headings(self):
    valid_heading = "# Valid1"
    valid_heading2 = "## Valid2"
    valid_heading3 = "### Valid3"
    valid_heading4 = "#### Valid4"
    valid_heading5 = "##### Valid5"
    valid_heading6 = "###### Valid6"
    self.assertEqual(block_to_block_type(valid_heading), block_type_heading)
    self.assertEqual(block_to_block_type(valid_heading2), block_type_heading)
    self.assertEqual(block_to_block_type(valid_heading3), block_type_heading)
    self.assertEqual(block_to_block_type(valid_heading4), block_type_heading)
    self.assertEqual(block_to_block_type(valid_heading5), block_type_heading)
    self.assertEqual(block_to_block_type(valid_heading6), block_type_heading)

  def test_block_to_block_type_code(self):
      valid_code = "``` valid code ```"
      self.assertEqual(block_to_block_type(valid_code), block_type_code)

  def test_block_to_block_type_quote(self):
    valid_quote = "> This is a quote"
    also_valid_quote = "> This is also a quote\n> with multiple lines"
    star_quote = "* This is a star quote"
    self.assertEqual(block_to_block_type(also_valid_quote), block_type_quote)
    self.assertEqual(block_to_block_type(star_quote), block_type_quote)


  def test_block_to_block_type_ordered_list(self):
    ordered_list = "1. This is an ordered list"
    ordered_list2 = "1. This is an ordered list\n 2. with multiple items"
    self.assertEqual(block_to_block_type(ordered_list), block_type_ordered_list)
    self.assertEqual(block_to_block_type(ordered_list2), block_type_ordered_list)
  
  def test_block_to_block_type_unordered_list(self):
    ul = "- invalid list"
    ul2 = "- startlist \n- foo"
    self.assertEqual(block_to_block_type(ul), block_type_unordered_list)
    self.assertEqual(block_to_block_type(ul2), block_type_unordered_list)

  def test_block_to_block_type_paragraph(self):
    paragraph = "This is a paragraph"
    self.assertEqual(block_to_block_type(paragraph), block_type_paragraph)

if __name__ == "__main__":
  unittest.main()
