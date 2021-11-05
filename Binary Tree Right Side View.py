class Solution:
	def rightSideView(self, root):
		if not root:
			return []

		result = [root.val]
		level = [root]

		while level:
			new_level = []
			for node in level:
				if node.left:
					new_level.append(node.left)
				if node.right:
					new_level.append(node.right)

			if new_level:
				result.append(new_level[-1].val)

			level = new_level
        
		return result
