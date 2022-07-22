# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Concept (left & right pointer, creating offset or gap b/w them)
        # take right pointer pointing to the head &
        # left pointer pointy to a dummy node, whose next will point head
        # move right pointer n times to make offset/gap b/w left & right
        # when right will reach at the end of the pointer
        # then at that time our left pointer will be one behind the element which we want to
        # delete bcz of dummy node
          
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # making offset or gap here b/w two pointers
        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        # delete
        left.next = left.next.next
        return dummy.next