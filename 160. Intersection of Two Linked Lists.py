# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        # Concept (Two Pointers pass the same distance in total)
        # Basically, make the two pointers pass the same distance in total, then they will
        # certainly meet. The meeting is either on a node or at the end (null). The total
        # distance passed will be m + n, as one pointer travels both the lists in no
        # intersection case.
        
        l1, l2 = headA, headB
        while l1!=l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        
        return l1