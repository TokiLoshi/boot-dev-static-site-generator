from textnode import TextNode

class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError

  def props_to_html(self):
    props_string = ""
    if self.props is None:
      return ""
    for prop in self.props:
      props_string += f' {prop}="{self.props[prop]}"'
    return props_string
  
  def __repr__(self):
    return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"


class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
    super().__init__(tag, value, None, props)

  def to_html(self):
    if self.value is None:
      raise ValueError("All leaf nodes require a value")
    if self.tag is None:
      return self.value
    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

  def __repr__(self):
    return f"LeafNode(tag: {self.tag}, value: {self.value}, props: {self.props})"  

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)

  def to_html(self):
    if self.tag is None:
      raise ValueError("All parent nodes require a tag")
    elif len(self.children) == 0:
      raise ValueError("All parent nodes require children")
    else:
      children_list = []
      for node in self.children:
        if node is None:
          continue
        children_list.append(node.to_html())
      children_string = "".join(children_list)
      props_html = self.props_to_html()
      final_html = f"<{self.tag}{props_html}>{children_string}</{self.tag}>"
      return final_html
      

  def __repr__(self):
    return f"ParentNode(tag: {self.tag}, children: {self.children}, props: {self.props})"