#Binary Tree Preorder Traversal, solved Nov 5 2024
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        if root == None: 
            return [] 
        order = [root.val]
        if (root.left != None): 
            order.extend(self.preorderTraversal(root.left))
        if (root.right != None): 
            order.extend(self.preorderTraversal(root.right))
        print(order)
        return order
        
