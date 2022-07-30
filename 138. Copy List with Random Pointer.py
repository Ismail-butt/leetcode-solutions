# https://leetcode.com/problems/copy-list-with-random-pointer/

# Question
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. 
# Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. 
# None of the pointers in the new list should point to nodes in the original list.

# Example
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        # Concept (First, Create the Copy of Curr/Old Link list nodes and save it in hash Map)
        # Use Two Loop (One for copy and Second for connecting)
        # first, Create Copy of nodes, Bcz we cannot connect random or next of copy to pointers/nodes of copy link list which are not created yet
        # Second, connect the pointers/nodes of copy link list
        
        oldToCopy = {None: None}
        
        # Cloning the link list node and adding it to hash Map
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        
        # Setting/Connecting the pointers of copy link list
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next] # Copy.next is pointing to the copy of curr.next
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        
        return oldToCopy[head]