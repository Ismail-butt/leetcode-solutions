# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Question
# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

# Example
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]

# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        # Concept (Make curr.next connection before going on to that node level)
        # try to visualize it on copy
        # First take curr, and nxt. After that connect curr.left.next to right by curr.left.next = curr.right
        # then check if curr.next is present, if it is present the connect curr.right.next by curr.right.next = curr.next.left
        # then move curr = curr.next, for BFS Approach
        # if it's none, then curr would be nxt which saved curr.left and nxt would be curr.left
        
        curr, nxt = root, root.left if root else None
        
        while curr and nxt:
            curr.left.next = curr.right           
            if curr.next:
                curr.right.next = curr.next.left
            
            curr = curr.next      
            if not curr:
                curr = nxt
                nxt = curr.left
        return root