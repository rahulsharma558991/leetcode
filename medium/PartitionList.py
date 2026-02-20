'''
Problem URL: https://leetcode.com/problems/partition-list/description/

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]

Constraints:
The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Approach: Two Pass Array based Partition
        # less: list[int] = []
        # greaterEqual: list[int] = []

        # # Traverse and partition into two arrays
        # while head is not None:
        #     if head.val < x:
        #         less.append(head.val)
        #     else:
        #         greaterEqual.append(head.val)
        #     head = head.next

        # # Create a new LinkedList with ordered elements
        # dummy = ListNode(0)
        # current = dummy
        # for num in less:
        #     current.next = ListNode(num)
        #     current = current.next
        # for num in greaterEqual:
        #     current.next = ListNode(num)
        #     current = current.next

        # return dummy.next




        # Approach: Two Pointer Single Pass
        # lessHead = ListNode(0)
        # greaterHead = ListNode(0)
        
        # less = lessHead
        # greater = greaterHead

        # # Partition list into less and greater lists
        # while head is not None:
        #     if head.val < x:
        #         # Append to less list
        #         less.next = head
        #         less = less.next
        #     else:
        #         # Append to greater list
        #         greater.next = head
        #         greater = greater.next
        #     head = head.next

        # # Important: break any existing pointers to ensure no cycles
        # greater.next = None
        # less.next = greaterHead.next

        # return lessHead.next





        # # Base case
        # if head is None:
        #     return None
        # # Initialize heads and tails for two separate lists
        # # h1/t1 for nodes < x (less)
        # # h2/t2 for nodes >= x (greater/equal)
        # h1 = t1 = h2 = t2 = None
        # while head:
        #     # Isolate the current node (temp)
        #     temp = head
        #     head = head.next
        #     temp.next = None
        #     # Check if the node belongs in the 'small' list
        #     if temp.val < x:
        #         if h1 is None:
        #             h1 = t1 = temp
        #         else:
        #             t1.next = temp
        #             t1 = temp
        #     # Otherwise, it belongs in the 'large/equal' list
        #     else:
        #         if h2 is None:
        #             h2 = t2 = temp
        #         else:
        #             t2.next = temp
        #             t2 = temp     
        # # --- MERGING THE LISTS ---
        # # Case 1: The small list is empty. 
        # # We just return the large list.
        # if h1 is None:
        #     return h2
        # # Case 2: The small list exists.
        # # Connect the tail of the small list (t1) to the head of the large list (h2)
        # t1.next = h2
        # return h1







        beforeList = beforeListHead = ListNode(-1)
        afterList = afterListHead = ListNode(-1)
        curr = head

        while (curr!=None):
            print(curr.val)
            if curr.val < x:
                beforeList.next = curr
                beforeList = curr
            else:
                afterList.next = curr
                afterList = curr
            
            curr = curr.next

        beforeList.next = afterListHead.next
        afterList.next = None

        return beforeListHead.next