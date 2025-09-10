class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        def preorder(node):
            if not node:
                return
            result.append(node.val)  
            preorder(node.left)      
            preorder(node.right)     
        preorder(root)
        return result
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
sol = Solution()
output = sol.preorderTraversal(root)
print("Preorder Traversal:", output)     