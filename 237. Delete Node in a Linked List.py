# https://leetcode.com/problems/delete-node-in-a-linked-list/

# Question
# Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, 
# instead you will be given access to the node to be deleted directly.
# It is guaranteed that the node to be deleted is not a tail node in the list.

# Example
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        # Concept (copy the value of next node and then delete next node)
        # Copy the value of next node and assign it to current node
        # then delete node.next
        
        node.val = node.next.val
        nxt = node.next.next
        node.next = nxt