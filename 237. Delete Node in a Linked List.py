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