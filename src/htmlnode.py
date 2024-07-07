class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError("to_html method not implemented")

  def props_to_html(self):
    if self.props is None:
      return ""
    props_string = ""
    for prop in self.props:
      props_string += f' {prop}="{self.props[prop]}"'
    return props_string
  
  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
    super().__init__(tag, value, None, props)

  # def __eq__(self, other):
  #   if isinstance(other, LeafNode):
  #     return (
  #       self.tag == other.tag,
  #       self.value == other.value,
  #       self.props == other.props
  #     )

  def to_html(self):
    print("self.props: ", self.props)
    props_string = ""
    if isinstance(self.props, dict):
      for prop in self.props:
        props_string += f" {prop}='{self.props[prop]}'"
    else:
      print("self.props is not a dictionary")
    return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"


    if self.value is None:
      raise ValueError("All leaf nodes require a value")
    if self.tag is None:
      return self.value
    return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

  def __repr__(self):
    return f"LeafNode({self.tag}, {self.value}, {self.props})"  

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)

  def __eq__(self, other):
    if isinstance(other, ParentNode):
      return (
        self.tag == other.tag, 
        self.children == other.children,
        self.props == other.props
      )
  def __repr__(self):
    return f"ParentNode(tag: {self.tag}, children: {self.children}, props: {self.props})"

  def to_html(self):
    if self.tag is None:
      raise ValueError("Invalid HTML: All parent nodes require a tag")
    if self.children is None:
      raise ValueError("Invalid HTML: All parent nodes require children")
    else:
      children_html = ""
      for child in self.children:
        children_html += child.to_html()
      return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
      

node = LeafNode("div", "example content", {"class": "example-class"})
print("DEBUGGING: ", node.to_html())