# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        auxList =[]
        self.preOrder(root,auxList)

        return auxList
    
    def preOrder(self, node, auxList):

        if node is None:
            return
        
        auxList.append(node.val)
        self.preOrder(node.left, auxList)
        self.preOrder(node.right, auxList)
        