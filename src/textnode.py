text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

from enum import Enum

class TextNodeType(Enum):
  TEXT = "text"
  BOLD = "bold"
  ITALIC = "italic"
  CODE = "code"
  LINK = "link"
  IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
       self.text = text
       self.text_type = text_type 
       self.url = url

    def __eq__(self, other):
      return (
        self.text == other.text 
        and self.text_type == other.text_type 
        and self.url == other.url
        )
      
    def __repr__(self):
      return f"TextNode({self.text}, {self.text_type}, {self.url})"

    
def text_node_to_html_node(text_node):
  from htmlnode import LeafNode
  match(text_node.text_type):
    case TextNodeType.TEXT:
      return LeafNode(None, text_node.text)
    case TextNodeType.BOLD:
      return LeafNode("b", text_node.text)
    case TextNodeType.ITALIC:
      return LeafNode("i", text_node.text)
    case TextNodeType.CODE:
      return LeafNode("code", text_node.text)
    case TextNodeType.LINK:
      return LeafNode("a", text_node.text, props={"href": text_node.url})
    case TextNodeType.IMAGE:
      return LeafNode("img", "", props={"src": text_node.url, "alt": text_node.text})
    case _:
      raise ValueError("Invalid text node type")

# def text_node_to_html_node(text_node):
#     if text_node.text_type == text_type_text:
#         return LeafNode(None, text_node.text)
#     if text_node.text_type == text_type_bold:
#         return LeafNode("b", text_node.text)
#     if text_node.text_type == text_type_italic:
#         return LeafNode("i", text_node.text)
#     if text_node.text_type == text_type_code:
#         return LeafNode("code", text_node.text)
#     if text_node.text_type == text_type_link:
#         return LeafNode("a", text_node.text, {"href": text_node.url})
#     if text_node.text_type == text_type_image:
#         return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
#     raise ValueError(f"Invalid text type: {text_node.text_type}")