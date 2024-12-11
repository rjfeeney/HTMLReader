from htmlnode import HTMLNode

class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag=tag, value=value, children=None, props=props)

	def to_html(self):
		if self.value == None and self.tag != "img":
			raise ValueError("Must have a value")
		if self.tag == None:
			return self.value
		if self.tag == "img":
			return f"<img src=\"{self.props['src']}\" alt=\"{self.props['alt']}\">"
		if self.props == None:
			return f"<{self.tag}>{self.value}</{self.tag}>"
		joined_props = []
		for key, value in self.props.items():
			joined = f' {key}="{value}"'
			joined_props.append(joined)
		result = "".join(joined_props)
		return f"<{self.tag}{result}>{self.value}</{self.tag}>"
