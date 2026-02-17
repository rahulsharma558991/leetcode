'''
Porblem URL: https://leetcode.com/problems/merge-k-sorted-lists/description/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #     if not l1:
    #         return l2
    #     if not l2:
    #         return l1

    #     if l1.val < l2.val:
    #         l1.next = self.mergeTwoLists(l1.next, l2)
    #         return l1
    #     else:
    #         l2.next = self.mergeTwoLists(l1, l2.next)
    #         return l2

    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     if not lists:
    #         return None
    #     return self.divideAndConquer(lists, 0, len(lists) - 1)

    # def divideAndConquer(self, lists: List[Optional[ListNode]], left: int, right: int) -> Optional[ListNode]:
    #     if left == right:
    #         return lists[left]

    #     mid = left + (right - left) // 2
    #     l1 = self.divideAndConquer(lists, left, mid)
    #     l2 = self.divideAndConquer(lists, mid + 1, right)
    #     return self.mergeTwoLists(l1, l2)




        # all_nums = []

        # for i in lists:

        #     cur = i
        #     while cur:
        #         all_nums.append(cur.val)
        #         cur = cur.next
        
        # all_nums = sorted(all_nums)
        
        # dummy = ListNode()
        # head = dummy
        # for i in all_nums:
        #     current = ListNode(i)
        #     head.next = current
        #     head = head.next

        # return dummy.next


        output = None
        curr = None
        lists = [ls for ls in lists if ls is not None]
        
        while lists:
            minnode_idx = min(range(len(lists)), key=lambda i: lists[i].val)
            if not output:
                output = lists[minnode_idx]
                curr = output
            else:
                curr.next = lists[minnode_idx]
                curr = curr.next

            if lists[minnode_idx].next:
                lists[minnode_idx] = lists[minnode_idx].next
            else:
                del lists[minnode_idx]

        return output
