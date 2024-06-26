from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode

def main():
  text_node1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
  html_node = HTMLNode("p", "This is text", [], {"href": "https://www.boot.dev"})
  leaf_node = LeafNode("p", "This is a paragraph of text.")
  leaf_node1 = LeafNode("a", "Click me!", {"href": "https://www.boot.dev"})
  print(text_node1)




main()
