class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root):
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val and
                    isMirror(t1.left, t2.right) and
                    isMirror(t1.right, t2.left))
        return isMirror(root, root)
node3_left = TreeNode(3)
node4_left = TreeNode(4)
node2_left = TreeNode(2, node3_left, node4_left)
node4_right = TreeNode(4)
node3_right = TreeNode(3)
node2_right = TreeNode(2, node4_right, node3_right)
root = TreeNode(1, node2_left, node2_right)
solution = Solution()
print("Is the tree symmetric?", solution.isSymmetric(root))