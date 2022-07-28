# https://leetcode.com/problems/remove-linked-list-elements/

# Question
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        # Concept (use dummy node, don't update prev for the node u are deleting)
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        
        while curr:
            nxt = curr.next         
            if curr.val == val:
                prev.next = nxt # We are not updating prev node here
            else:
                prev = curr
                
            curr = nxt
        return dummy.next