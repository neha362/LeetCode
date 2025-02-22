# Recover a Tree From Preorder Traversal, solved Feb 22 2025

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = collections.deque()
        tree = None
        #while the string still contains characters, parses the next value and the next depth
        while traversal:
            depth = self.numDepth(traversal)
            traversal = traversal[depth:]
            ind = self.getNextNum(traversal)
            num = int(traversal[:ind])
            traversal = traversal[ind:]
            tree = TreeNode(num, None, None)
            #if the stack is empty, that means that the first node still needs to be added to the list
            if not stack:
                stack.append((depth, tree))
                continue
            #if the current node has the same depth as the above node, we need to swap out the current node (which is the left node) for the new node (which is the right node)
            if stack[-1][0] == depth:
                stack.pop()
                stack[-1][1].right = tree
                stack.append((depth, tree))
            #if the current node is of a deeper depth than the new node, a new branch is being explored, so we need to pop the elements of the stack until the branches are level, then swap out the left and right branches
            elif stack[-1][0] > depth:
                while stack[-1][0] > depth:
                    stack.pop()
                stack.pop()
                stack[-1][1].right = tree
                stack.append((depth, tree))
            #if the node is of a deeper depth than the previous node, it must be the left successor
            else:
                stack[-1][1].left = tree
                stack.append((depth, tree))
        #returns the base node of the stack
        return stack[[0][1]]

    #parses the number of dashes in the string and returns the new index of the next number
    def numDepth(self, string):
        if string == "":
            return -1
        index = 0
        while string[index] == "-":
            index += 1
        return index
    
    #parses the number of continuous numbers in the string and returns the index of the next dash
    def getNextNum(self, string):
        index = 0
        while index < len(string) and string[index].isnumeric():
            index += 1
        return index
