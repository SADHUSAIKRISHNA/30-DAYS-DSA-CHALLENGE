class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        return (root.val +
                self.rangeSumBST(root.left, low, high) +
                self.rangeSumBST(root.right, low, high))
root = TreeNode(10)
root.left = TreeNode(5, TreeNode(3), TreeNode(7))
root.right = TreeNode(15, None, TreeNode(18))
sol = Solution()
low, high = 7, 15
print("Range Sum BST:", sol.rangeSumBST(root, low, high))  