# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {}
        
        for i, node in enumerate(inorder):
            idx[node] = i
        
        stack = []
        head = None
        
        for val in preorder:
            if not head:
                head = TreeNode(val)
                stack.append(head)
            else:
                node = TreeNode(val)
                if idx[val] < idx[stack[-1].val]:
                    stack[-1].left = node
                else:
                    while stack and idx[val] > idx[stack[-1].val]:
                        u = stack.pop()
                    u.right = node
                stack.append(node)
        return head
                    
