# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        # Concept (save curr.next in nxt before giving it the value of Prev)
        # take prev and curr, assign them none & head
        # save curr.next in nxt & then give curr.next the prev node.
        
        prev, curr = None, head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        return prev