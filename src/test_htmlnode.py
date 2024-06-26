import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, TextNodeType
from textnode import TextNode

class TestHTMLNode(unittest.TestCase):
  def test_init(self):
    html_node = HTMLNode()
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, None)

  def test_repr(self):
    html_node = HTMLNode("p", "This is text", [], {"href": "https://www.boot.dev"})
    self.assertEqual("HTMLNode(tag: p, value: This is text, children: [], props: {'href': 'https://www.boot.dev'})", repr(html_node))

  def test_props_to_html_empty(self):
    html_node = HTMLNode(props={})
    self.assertEqual(html_node.props_to_html(), "")

  def test_props_to_html_multiple(self):
    html_node = HTMLNode(props={"href": "https://www.boot.dev", "target": "_blank"})
    self.assertEqual(html_node.props_to_html(), ' href="https://www.boot.dev" target="_blank"')

  def test_children_handling(self):
    child_node = HTMLNode("span", "child text")
    parent_node = HTMLNode("div", children=[child_node])
    self.assertEqual(parent_node.children, [child_node])

class TestLeafNode(unittest.TestCase):
  def test_leaf_init(self):
    leaf_node = LeafNode("p", "This is a paragraph")
    leaf_node1 = LeafNode("a", "Visit Boots!", {"href": "http://www.boot.dev"})
    self.assertEqual(leaf_node.tag, "p")
    self.assertEqual(leaf_node.value, "This is a paragraph")
    self.assertEqual(leaf_node1.props["href"], "http://www.boot.dev")

  def test_to_html(self):
    leaf_node = LeafNode("p", "This is a paragraph")
    self.assertEqual(leaf_node.to_html(), "<p>This is a paragraph</p>")

def test_to_html_empty(self):
  empty_leaf_node = LeafNode("p", None)
  with self.assertRaises(ValueError):
    empty_leaf_node.to_html()

class TestParentNode(unittest.TestCase):
  def test_parent_init(self):
    parent_node = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")])
    self.assertEqual(parent_node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")


if __name__ == "__main__":
  unittest.main()