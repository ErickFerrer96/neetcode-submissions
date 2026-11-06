# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0

        self.getHeight(root)

        return self.diameter

    def getHeight(self, root):

        if root is None:
            return 0
        
        depthLeft = self.getHeight(root.left)
        depthRight = self.getHeight(root.right)

        if self.diameter < (depthLeft + depthRight):
            self.diameter = depthLeft + depthRight

        return max (depthLeft, depthRight) + 1
            






        