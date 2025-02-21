#Find Elements in a Contaminated Binary Tree, solved 2/20/2025

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = {0:None}
        curr_nodes = [root]
        root.val = 0
        while curr_nodes:
            if curr_nodes[0].left != None:
                curr_nodes[0].left.val = 2 * curr_nodes[0].val + 1
                self.nodes[curr_nodes[0].left.val] = curr_nodes[0].val
                curr_nodes.append(curr_nodes[0].left)
            if curr_nodes[0].right != None:
                curr_nodes[0].right.val = 2 * curr_nodes[0].val + 2
                self.nodes[curr_nodes[0].right.val] = curr_nodes[0].val
                curr_nodes.append(curr_nodes[0].right)
            curr_nodes.pop(0)

    def find(self, target: int) -> bool:
        return target in self.nodes


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
