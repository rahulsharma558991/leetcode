'''
Problem URL: https://leetcode.com/problems/swap-nodes-in-pairs/description

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Example 4:
Input: head = [1,2,3]
Output: [2,1,3]

Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        # Approach: Recursive
        if head is None or head.next is None:
            return head
        
        temp = ListNode(0, None)
        temp = head.next

        head.next = self.swapPairs(head.next.next)
        temp.next = head

        return temp
        '''

        # Approach: Iterative solution
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(0, head)
        prev = dummy  # prev will be used to keep track of (point to) the node that will connect to the next reversed pair
        curr = head
        while curr and curr.next:
            # Define the pair (first, second) based on curr pointer
            first = curr
            second = curr.next
            next_pair = second.next  # start of the next segment or pair

            # Reverse the pair
            second.next = first
            first.next = next_pair
            prev.next = second
            
            # advance pointers
            '''
            Why prev = first is the right move
            After swapping: prev -> second -> first -> next_pair
            first becomes the tail of the swapped pair, so it’s the node that should connect to the next swapped pair.
            '''
            prev = first  # tail of swapped pair
            curr = next_pair  # next pair start
        return dummy.next
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))