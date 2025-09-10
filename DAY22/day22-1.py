class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)       
            result.append(node.val)  
            inorder(node.right)     
        inorder(root)
        return result
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
sol = Solution()
output = sol.inorderTraversal(root)
print("Inorder Traversal:", output)     