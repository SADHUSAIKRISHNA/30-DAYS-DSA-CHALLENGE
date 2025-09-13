class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def is_leaf(node):
            return node and not node.left and not node.right
        def dfs(node):
            if not node:
                return 0
            left_sum = 0
            if is_leaf(node.left):
                left_sum += node.left.val
            return left_sum + dfs(node.left) + dfs(node.right)
        return dfs(root)
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))
sol = Solution()
print("Sum of left leaves:", sol.sumOfLeftLeaves(root)) 