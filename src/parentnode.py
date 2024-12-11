from htmlnode import HTMLNode

class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag, None, children, props)

	def to_html(self):
		if self.tag == None:
			raise ValueError("Must have a tag")
		if len(self.children) == 0:
			raise ValueError("Must have children")
		children_list = []
		for child in self.children:
			children_list.append(child.to_html())
		joined_children = "".join(children_list)
		return f"<{self.tag}{self.props_to_html()}>{joined_children}</{self.tag}>"
