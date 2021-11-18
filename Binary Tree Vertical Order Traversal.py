# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        col_table = defaultdict(list)
        queue = deque([(root, 0, 0)])
        min_col = max_col = 0
        
        while queue:
            node, row, col = queue.popleft()
            if node is not None:
                col_table[col].append((row, node.val))
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                
                queue.append((node.left, row + 1, col - 1))
                queue.append((node.right, row + 1, col + 1))
        
        res = []
        for x in range(min_col, max_col + 1):
            #col_table[x].sort(key = lambda k: (k[0], k[1]))
            res.append([level[1] for level in col_table[x]])
            
        return res
