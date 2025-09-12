class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        self.max_diameter = 0
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.max_diameter = max(self.max_diameter, left + right)
            return 1 + max(left, right)
        depth(root)
        return self.max_diameter
node4 = TreeNode(4)
node5 = TreeNode(5)
node2 = TreeNode(2, node4, node5)
node3 = TreeNode(3)
root = TreeNode(1, node2, node3)
solution = Solution()
print("Diameter of the binary tree is:", solution.diameterOfBinaryTree(root))