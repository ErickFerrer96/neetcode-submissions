# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.balanced = True
        self.checkBalance(root)

        return self.balanced
    
    def checkBalance(self, root):

        if root is None:
            return 0

        depthLeft = self.checkBalance(root.left)
        depthRight = self.checkBalance(root.right)

        if abs(depthLeft - depthRight) > 1:

            self.balanced = False
        
        return max (depthLeft, depthRight) + 1
        

