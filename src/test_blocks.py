import unittest
from blocks import markdown_to_blocks

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

if __name__ == "__main__":
  unittest.main()
