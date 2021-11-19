# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.inorder_list = []
        self.idx = 0
        self.root = root
        self.inorder(self.root)
        
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.inorder_list.append(root.val)
        self.inorder(root.right)

    def next(self) -> int:
        self.idx += 1
        return self.inorder_list[self.idx - 1]

    def hasNext(self) -> bool:
        return self.idx < len(self.inorder_list)
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
