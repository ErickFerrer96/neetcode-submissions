# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        auxList =[]
        self.postOrder(root,auxList)

        return auxList
    
    def postOrder(self, node, auxList):

        if node is None:
            return
        
        self.postOrder(node.left, auxList)
        self.postOrder(node.right, auxList)
        auxList.append(node.val)