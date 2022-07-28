# https://leetcode.com/problems/odd-even-linked-list/

# Questions
# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# Example
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        # Concept(Odd & Even List, merge)
        # Take odd and even list
        # start count = 1 bcz The first node is considered odd
        # then if count is even then add to even list else viceversa
        # at the end, Merge the odd and even list
        
        odd_head = ListNode(0)
        odd = odd_head
        
        even_head = ListNode(0)
        even = even_head
        
        count = 1 # bcz The first node is considered odd
        while head:
            if count % 2 == 0:
                even.next = head
                even = even.next
            else:
                odd.next = head
                odd = odd.next
            
            count += 1
            head = head.next
        
        even.next = None
        odd.next = even_head.next
        
        
        return odd_head.next