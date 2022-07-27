# https://leetcode.com/problems/sort-list/

# Question
# Given the head of a linked list, return the list after sorting it in ascending order.

# Example
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortList(self, head):
        # Concept (Merge Sort(OlogN))
        # Divide the list in two untill we reach one node in the link list
        # then start merging the last two link list in sorting order
        # and that's it :)
        
        if not head or not head.next:
            return head
        
        # Split the list in two halfs
        left = head
        right = self.getMid(head)
        nxt = right.next
        right.next = None
        right = nxt
        
        left = self.sortList(left)
        right = self.sortList(right)
        # Merge both lists in Sorting Order
        return self.merge(left, right)
    
    def getMid(self, head):
        # Remember Fast.next
        slow, fast = head, head.next   
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next