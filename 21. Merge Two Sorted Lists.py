# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Concept
        # while list1 and list not equal to NULL,
        # check if list1.value is smaller then list2.value
        # if this happens then add list1 to your output link list and move l1 to next & Vice versa
        
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
        
        # if list1 or list2 is not NULL, then
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next