'''
Problem URL: https://leetcode.com/problems/reverse-linked-list-ii/description/

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

Follow up: Could you do it in one pass?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # if not head or left == right:
        #     return head
        
        # dummy = ListNode(0, head)
        # prev = dummy
        
        # for _ in range(left - 1):
        #     prev = prev.next
        
        # current = prev.next
        
        # for _ in range(right - left):
        #     next_node = current.next
        #     current.next, next_node.next, prev.next = next_node.next, prev.next, next_node

        # return dummy.next






        # if not head.next:
        #     return head
        
        # i = 1
        # start = None
        # cur = head

        # while i<left and cur:
        #     start = cur
        #     cur = cur.next
        #     i+=1

        # end = cur
        # prev = None
        # while cur and i<=right:
        #     tmp = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = tmp
        #     i+=1
        
        # if start:
        #     start.next = prev
        # else:
        #     head = prev

        # if end:
        #     end.next = cur

        # return head








    #     h=ListNode(-600)
    #     h.next=head
    #     pom=h
    #     for i in range(left-1):
    #         pom=pom.next
    #     list1=pom.next
    #     tail1=pom
    #     pom=list1
    #     for i in range(right-left):
    #         pom=pom.next
    #     tail2=pom.next
    #     pom.next=None

    #     list1=self.reverseList(list1)
    #     tail1.next=list1
    #     while list1.next:
    #         list1=list1.next
    #     list1.next=tail2
    #     return h.next

    # def reverseList(self, head) -> Optional[ListNode]:
        
    #     prev,curr=None,head

    #     while curr:
    #         pom=curr.next
    #         curr.next=prev
    #         prev=curr
    #         curr=pom
    #     return prev









        # if not (head and left < right):
        #     return head

        # def helper(node, m):
        #     nonlocal left, right
        #     if m == left:
        #         prev = None
        #         current = node
        #         while m <= right:
        #             current.next, prev, current = prev, current, current.next
        #             m += 1
        #         node.next = current
        #         return prev
        #     elif m < left:
        #         node.next = helper(node.next, m + 1)
        #     return node

        # return helper(head, 1)









        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        stack = []
        current = prev.next

        for _ in range(right - left + 1):
            stack.append(current)
            current = current.next

        while stack:
            prev.next = stack.pop()
            prev = prev.next

        prev.next = current

        return dummy.next