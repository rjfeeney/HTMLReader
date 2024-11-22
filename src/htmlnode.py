
class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def __eq__(self, other):
		if isinstance(other, HTMLNode):
			return (
				self.tag == other.tag and
				self.value == other.value and
				self.props == other.props
			)
		return False

	def to_html(self):
		raise NotImplementedError

	def props_to_html(self):
		if self.props == None:
			return ""
		joined_htmls = []
		for key, value in self.props.items():
			joined = f' {key}="{value}"'
			joined_htmls.append(joined)
		result = "".join(joined_htmls)
		return result

	def __repr__(self):
		return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
