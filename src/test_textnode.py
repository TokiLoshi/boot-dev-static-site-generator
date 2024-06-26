import unittest

from textnode import (
  TextNode,
  text_type_text,
  text_type_bold,
  text_type_italic,
  text_type_code,
  text_type_link,
  text_type_image
)

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", "bold")
    node2 = TextNode("This is a text node", "bold")
    node3 = TextNode("This is a text node", "bold", None)
    self.assertEqual(node, node2)
    self.assertEqual(node, node3)
  
  def test_same_url(self):
    node = TextNode("This is a text node", "italic", "https://www.boot.dev")
    node2 = TextNode("This is a text node", "italic", "https://www.boot.dev")
    self.assertEqual(node, node2)

  def test_different_url(self):
    node = TextNode("This is a text node", "bold")
    node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    self.assertNotEqual(node, node2)

  def test_type(self):
    node = TextNode("This is a text node", "bold")
    node2 = TextNode("This is a text node", "italic")
    self.assertNotEqual(node, node2)

  def test_text(self):
    node = TextNode("This is a text node", "bold")
    node2 = TextNode("This is a different text node", "bold")
  
  def test_repr(self):
    node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
    self.assertEqual("TextNode(This is a text node, text, https://www.boot.dev)", repr(node))
  
  # def test_convert_text_node(self):
  #   text_type_text = "text"
  #   text_type_bold = "bold"
  #   text_type_italic = "italic"
  #   text_type_code = "code"
  #   text_type_link = "link"
  #   text_type_image = "image"
  #   text_type_wrong = "wrong"
  #   text_node_text = TextNode(TextNodeType.TEXT, "This is a paragraph")
  #   text_node_bold = TextNode(TextNodeType.BOLD, "This is bold text")
  #   text_node_italic = TextNode(TextNodeType.ITALIC, "This is italic text")
  #   text_node_code = TextNode(TextNodeType.CODE, "This is code")
  #   text_node_link = TextNode(TextNodeType.LINK, "This is a link", {"href": "http://www.boot.dev"})
  #   text_node_image = TextNode(TextNodeType.IMAGE, None, {"src": "http://www.boot.dev", "alt": "Boots Logo"})
  #   self.assertEqual(self.text_node_to_html_node(text_node_text), LeafNode(None, "This is a paragraph"))
    # self.assertEqual(self.text_node_to_html_node(text_node_bold), "<b>This is bold text</b>")

  if __name__ == "__main__:":
    unittest.main()