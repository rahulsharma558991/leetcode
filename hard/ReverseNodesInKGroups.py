'''
Problem URL: https://leetcode.com/problems/reverse-nodes-in-k-group/description/

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000

Follow-up: Can you solve the problem in O(1) extra memory space?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if not head:
        #     return None

        # tail = head

        # for _ in range(k):
        #     if not tail:
        #         return head
        #     tail = tail.next

        # def reverse(cur, end):
        #     prev = None

        #     while cur != end:
        #         next = cur.next
        #         cur.next = prev
        #         prev = cur
        #         cur = next

        #     return prev      

        # new_head = reverse(head, tail)
        # head.next = self.reverseKGroup(tail, k)

        # return new_head 





        dummy = ListNode(0, head)
        group_prev = dummy

        def get_kth_node(start: ListNode, k: int):
            while start and k > 0:
                start = start.next
                k -= 1
            
            return start

        while True:
            # Find the k-th node from group_prev
            kth_node = get_kth_node(group_prev, k)
            if not kth_node:
                break
            group_next = kth_node.next

            # Reverse the group
            prev, cur = kth_node.next, group_prev.next
            while cur != group_next:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            # Reconnect the reversed group with the rest of the list
            temp = group_prev.next
            group_prev.next = kth_node
            group_prev = temp

        return dummy.next           