import unittest

from inline_markdown import split_nodes_delimiter, extract_markdown_links, extract_markdown_images, split_nodes_link, split_nodes_images, text_to_textnodes

from textnode import (
  TextNode,
  text_type_text,
  text_type_bold,
  text_type_italic,
  text_type_code,
  text_type_link,
  text_type_image
)

class TestInlineMarkdown(unittest.TestCase):
  def test_delimiter_bold(self):
    node = TextNode("This is text with a **bolded** word", text_type_text)
    new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
    self.assertEqual([TextNode("This is text with a ", text_type_text), TextNode("bolded", text_type_bold), TextNode(" word", text_type_text)], new_nodes)
  
  def test_delimiter_italic(self):
    node = TextNode("This is text with an *italicized* word", text_type_text)
    new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
    self.assertEqual([TextNode("This is text with an ", text_type_text), TextNode("italicized", text_type_italic), TextNode(" word", text_type_text)], new_nodes)

  def test_delimiter_code(self):
    node = TextNode("This is text with a `code block` word", text_type_text)
    new_nodes = split_nodes_delimiter([node], "`", text_type_code)
    self.assertEqual([TextNode("This is text with a ", text_type_text), TextNode("code block", text_type_code), TextNode(" word", text_type_text)], new_nodes)

  def test_delimiter_invalid(self):
    node = TextNode("This is text with a `code block word", text_type_text)
    with self.assertRaises(ValueError):
      split_nodes_delimiter([node], "`", text_type_code)


class TestLinkExtractor(unittest.TestCase): 
  def test_extract_markdown_links(self):
    text = "This is a [link](https://www.example.com)"
    links = extract_markdown_links(text)
    self.assertEqual([("link", "https://www.example.com")], links)
  def test_extract_markdown_images(self):
    text = text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
    images = extract_markdown_images(text)
    self.assertListEqual([("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")], images)

  def test_split_image_node(self):
    single_image_node = [TextNode("Text with one image ![image](https://boot.dev/bootsiscute)", text_type_text)]
    self.assertEqual([TextNode("Text with one image ", text_type_text), TextNode("image", text_type_image, "https://boot.dev/bootsiscute")], split_nodes_images(single_image_node))

  def test_split_link_node(self):
    single_link_node = [TextNode("Text with one link [link](https://boot.dev/bootsiscute)", text_type_text)]
    self.assertEqual([TextNode("Text with one link ", text_type_text), TextNode("link", text_type_link, "https://boot.dev/bootsiscute")], split_nodes_link(single_link_node))

class TestTextToTextNodes(unittest.TestCase):
  def test_text_to_text_nodes(self):
    text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
    self.assertEqual([
      TextNode("This is ", text_type_text),
      TextNode("text", text_type_bold),
      TextNode(" with an ", text_type_text),
      TextNode("italic", text_type_italic),
      TextNode(" word and a ", text_type_text),
      TextNode("code block", text_type_code),
      TextNode(" and an ", text_type_text),
      TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
      TextNode(" and a ", text_type_text),
      TextNode("link", text_type_link, "https://boot.dev")
    ], text_to_textnodes(text))

if __name__ == "__main__":
  unittest.main()