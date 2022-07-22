# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        # Concept (Slow pointer and Fast pointer)
        # increase slow ptr by one and fast by two
        # if slow and fast becomes equal, then there is a loop
        # if fast & fast.next, got equal to None/NULL, then no loop
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False