# https://leetcode.com/problems/palindrome-linked-list/

# Question
# Given the head of a singly linked list, return true if it is a palindrome.

# Example
# Input: head = [1,2,2,1]
# Output: true

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        # Concept (Reverse Second half of link list)
        # Find middle node
        # then reverse second half
        # Now, use left & right pointer to check for palindrome
        
        slow, fast = head, head
        
        # find middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse second half
        prev, curr = None, slow       
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Check Palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True