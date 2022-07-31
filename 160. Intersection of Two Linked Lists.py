# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Question
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
# If the two linked lists have no intersection at all, return null.

# Example
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Intersected at '8'
# Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
# From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

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