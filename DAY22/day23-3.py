class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        def postorder(node):
            if not node:
                return
            postorder(node.left)      
            postorder(node.right)     
            result.append(node.val)   

        postorder(root)
        return result
# Create the tree structure
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
# Call the function
sol = Solution()
output = sol.postorderTraversal(root)
print("Postorder Traversal:", output)         