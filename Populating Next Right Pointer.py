"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        queue = [root]
        while queue:
            level = []
            for i in range(len(queue)):
                if queue[i].left:
                    level.append(queue[i].left)
                if queue[i].right:
                    level.append(queue[i].right)
                if i == len(queue) - 1:
                    queue[i].next = None
                elif i < len(queue) - 1:
                    queue[i].next = queue[i+1]
            queue = level
        return root
