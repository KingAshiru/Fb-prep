# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        if not root:
            return 0
        
        def dfs(node):
            
            # if node is None, return 0 as sum and 0 as no. of nodes
            if node is None:
                return (0, 0)
            
            # go to left subtree and get total sum on that subtree, and the total nodes
            sum_left, node_cnt_left = dfs(node.left)
            
            # go to right subtree and get total sum on that subtree, and the total nodes
            sum_right, node_cnt_right = dfs(node.right)
            
            # calculate the total sum
            _total_sum = node.val + sum_left + sum_right
            # calculate the total no. of nodes
            _total_nodes = 1 + node_cnt_left + node_cnt_right
            # compute the avg
            _avg = _total_sum / _total_nodes
            
            # update max_avg if it is smaller than computed avg
            if _avg > self.max_avg:
                self.max_avg = _avg
            
            # return the total sum and total nodes to previous stack call.
            return (_total_sum, _total_nodes)
        
        # set a variable to track max_avg
        self.max_avg = float("-inf")
        dfs(root)

        return self.max_avg
