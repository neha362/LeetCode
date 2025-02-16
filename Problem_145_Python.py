#Binary Tree Postorder Traversal, Nov 5 2024
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        order = []
        if (root == None): 
            return order
        if (root.left != None):
            order.extend(self.postorderTraversal(root.left))
        if (root.right != None): 
            order.extend(self.postorderTraversal(root.right))
        order.append(root.val)
        return order
