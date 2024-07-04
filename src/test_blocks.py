import unittest
from blocks import (
  markdown_to_blocks, 
  block_to_block_type, 
  block_type_heading, 
  block_type_quote, 
  block_type_code, 
  block_type_ordered_list, 
  block_type_unordered_list, 
  block_type_paragraph,
  heading_markdown_block_to_html_node,
  quote_markdown_block_to_html_node,
  code_markdown_block_to_html_node,
  paragraph_markdown_to_html_node,
  unordered_list_markdown_to_html_node,
  ordered_list_markdown_to_html_node,
  markdown_to_html_node
  )
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestMarkdownToBlocks(unittest.TestCase):
  def test_markdown_to_blocks(self):
    markdown = """
               # This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
              """
    blocks = markdown_to_blocks(markdown)
    self.assertEqual(
          blocks, 
            [
                "# This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items"
            ]
        )

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
    single_line_unordered_list = "- unordered_list list"
    multi_line_unordered_list = "- startlist \n- foo"
    self.assertEqual(block_to_block_type(single_line_unordered_list), block_type_unordered_list)
    self.assertEqual(block_to_block_type(multi_line_unordered_list), block_type_unordered_list)

  def test_block_to_block_type_paragraph(self):
    paragraph = "This is a paragraph"
    self.assertEqual(block_to_block_type(paragraph), block_type_paragraph)

class TestBlockTypeToHTMLNode(unittest.TestCase):
  def test_heading_markdown_block_to_html_node(self):
    heading1 = "# Should be an h1"
    heading2 = "## Should be an h2"
    heading3 = "### Should be an h3"
    heading4 = "#### Should be an h4"
    heading5 = "##### Should be an h5"
    heading6 = "###### Should be an h6"

    # Expected Leafnodes: 
    expected1 = LeafNode("h1", "Should be an h1", block_type_heading)
    expected2 = LeafNode("h2", "Should be an h2", block_type_heading)
    expected3 = LeafNode("h3", "Should be an h3", block_type_heading)
    expected4 = LeafNode("h4", "Should be an h4", block_type_heading)
    expected5 = LeafNode("h5", "Should be an h5", block_type_heading)
    expected6 = LeafNode("h6", "Should be an h6", block_type_heading)
    self.assertEqual(heading_markdown_block_to_html_node(heading1, block_type_heading), expected1)
    self.assertEqual(heading_markdown_block_to_html_node(heading1, block_type_heading), expected2)
    self.assertEqual(heading_markdown_block_to_html_node(heading1, block_type_heading), expected3)
    self.assertEqual(heading_markdown_block_to_html_node(heading1, block_type_heading), expected4)
    self.assertEqual(heading_markdown_block_to_html_node(heading1, block_type_heading), expected5)
    self.assertEqual(heading_markdown_block_to_html_node(heading1, block_type_heading), expected6)

  def test_quote_markdown_block_to_html_node(self):
    single_line_quote = "> Single line quote"
    multi_line_quote = "> Multi line quote\n> with multiple lines"
    single_star_quote = "* Single line star quote"
    multi_line_star_quote = "* Multi line star quote\n* double double toil and trouble"
    
    expected_single_quote = LeafNode("blockquote", "Single line quote", block_type_quote)
    expected_multi_line_quote = LeafNode("blockquote", "Multi line quote\n> with multiple lines", block_type_quote)
    expected_single_star_quote = LeafNode("blockquote", "Single line star quote", block_type_quote)
    expected_multi_line_star_quote = LeafNode("blockquote", "Multi line star quote\n* double double toil and trouble", block_type_quote)
    
    self.assertEqual(quote_markdown_block_to_html_node(single_line_quote, block_type_quote), expected_single_quote)
    self.assertEqual(quote_markdown_block_to_html_node(multi_line_quote, block_type_quote), expected_multi_line_quote)
    self.assertEqual(quote_markdown_block_to_html_node(single_star_quote, block_type_quote), expected_single_star_quote)
    self.assertEqual(quote_markdown_block_to_html_node(multi_line_star_quote, block_type_quote), expected_multi_line_star_quote)

  def test_code_markdown_block_to_html_node(self):
    code = "```Hello world```"
    expected_code = LeafNode("code", "Hello world", block_type_code)
    expected_parent = ParentNode("pre", [expected_code])
    self.assertEqual(code_markdown_block_to_html_node(code, block_type_code), expected_parent)

  def test_unordered_list_markdown_to_html_node(self):
    inner_list = "- This is an unordered list"
    inner_list2 = "- This is an unordered list\n- with multiple items"  

    expected_parent_1 = ParentNode("ul", [LeafNode("li", "This is an unordered list", block_type_unordered_list)])
    expected_parent_2 = ParentNode("ul", [LeafNode("li", "This is an unordered list"), LeafNode("li", "with multiple items")], block_type_unordered_list)
    self.assertEqual(unordered_list_markdown_to_html_node(inner_list, block_type_unordered_list), expected_parent_1)
    self.assertEqual(unordered_list_markdown_to_html_node(inner_list2, block_type_unordered_list), expected_parent_2)

  def test_ordered_list_markdown_to_html_node(self):
    inner_list = "1. This is an ordered list"
    inner_list_multiple_lines = "1. This is an ordered list\n2. and it has multiple lines"

    expected_parent_1 = ParentNode("ol", [LeafNode("li", "This is an ordered list", block_type_ordered_list)])
    expected_parent_2 = ParentNode("ol", [LeafNode("li", "This is an ordered list"), LeafNode("li", "and it has multiple lines", block_type_ordered_list)])
    
    self.assertEqual(ordered_list_markdown_to_html_node(inner_list, block_type_ordered_list), expected_parent_1)
    self.assertEqual(ordered_list_markdown_to_html_node(inner_list_multiple_lines, block_type_ordered_list), expected_parent_2)
  
  def test_paragraph_markdown_to_html_node(self):
    text = "This is a paragraph"
    expected = LeafNode("p", "This is a paragraph", block_type_paragraph)
    self.assertEqual(paragraph_markdown_to_html_node(text, block_type_paragraph), expected)

class TestMarkdownToHTML(unittest.TestCase):
  def test_markdown_to_html(self):
    markdown = "# h1"
    expected = ParentNode("div", [LeafNode("h1", "h1", block_type_heading)])
    self.assertEqual(markdown_to_html_node(markdown), expected)

if __name__ == "__main__":
  unittest.main()
