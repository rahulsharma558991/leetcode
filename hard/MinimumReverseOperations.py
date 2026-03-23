'''
Problem URL:

You are given an integer n and an integer p representing an array arr of length n where all elements are set to 0's, except position p which is set to 1. You are also given an integer array banned containing restricted positions. Perform the following operation on arr:
Reverse a subarray with size k if the single 1 is not set to a position in banned.
Return an integer array answer with n results where the ith result is the minimum number of operations needed to bring the single 1 to position i in arr, or -1 if it is impossible.

Example 1:
Input: n = 4, p = 0, banned = [1,2], k = 4
Output: [0,-1,-1,1]
Explanation:
Initially 1 is placed at position 0 so the number of operations we need for position 0 is 0.
We can never place 1 on the banned positions, so the answer for positions 1 and 2 is -1.
Perform the operation of size 4 to reverse the whole array.
After a single operation 1 is at position 3 so the answer for position 3 is 1.

Example 2:
Input: n = 5, p = 0, banned = [2,4], k = 3
Output: [0,-1,-1,-1,-1]
Explanation:
Initially 1 is placed at position 0 so the number of operations we need for position 0 is 0.
We cannot perform the operation on the subarray positions [0, 2] because position 2 is in banned.
Because 1 cannot be set at position 2, it is impossible to set 1 at other positions in more operations.

Example 3:
Input: n = 4, p = 2, banned = [0,1,3], k = 1
Output: [-1,-1,0,-1]
Explanation:
Perform operations of size 1 and 1 never changes its position.

Constraints:
1 <= n <= 105
0 <= p <= n - 1
0 <= banned.length <= n - 1
0 <= banned[i] <= n - 1
1 <= k <= n 
banned[i] != p
all values in banned are unique 
'''

# class Solution:
#     def minReverseOperations(self, n: int, p: int, banned_val: List[int], K: int) -> List[int]:
#         remaining = [SortedList(), SortedList()]
#         banned = set(banned_val)
#         for u in range(n):
#             if u != p and u not in banned:
#                 remaining[u & 1].add(u)

#         queue = [p]
#         dist = [-1] * n
#         dist[p] = 0
#         for node in queue:
#             lo = max(node - K + 1, 0)
#             lo = 2 * lo + K - 1 - node
#             hi = min(node + K - 1, n - 1) - (K - 1)
#             hi = 2 * hi + K - 1 - node

#             for nei in list(remaining[lo % 2].irange(lo, hi)):
#                 queue.append(nei)
#                 dist[nei] = dist[node] + 1
#                 remaining[lo % 2].remove(nei)
        
#         return dist









# class Solution:
#     def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
#         ans = [-1]*n
#         ban = set(banned)
#         queue = [p]
#         l = 0
#         while queue:
#             new = []
#             left, right = n, -1
#             for curr in queue:
#                 ans[curr] = l
#                 left =  min(left,  2* max(curr - k + 1, 0) + k -1 -curr)
#                 right = max(right, 2* min(n-k,curr) + k -1 -curr)
#             for i in range(left, right+1, 2):
#                 if ans[i] == -1 and i not in ban:
#                     new.append(i)
#             queue = new
#             l += 1
#         return ans









# class Solution:
#     def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
#         out = [-1] * n
#         # To speed up iterations, mark banned positions differently; remember to
#         # convert them to -1 at the end.
#         for node in banned:
#             out[node] = -2
#         # Perform reversals in level-based breadth-first order.
#         nodes = [p]
#         depth = 0
#         out[p] = depth
#         step = k - 1
        
#         # TLEs occur when n is large, k is large, and not to many are banned,
#         # so that very O(N) points have O(N) possible post-reverse positions.
#         # These O(N) post-reverse positions are 2 apart, but each only needs
#         # to be visited once. We will nextNode2s dynamically to save work.
#         nextNode2s = [i + 2 for i in range(n)]  # might be out of range

#         while nodes:
#             depth += 1
#             newNodes = []
#             for node1 in nodes:
#                 # The post-reverse positions are every other node between
#                 # loNode2 and hiNode2, inclusive.
#                 loReverseStart = max(node1 - step, 0)
#                 hiReverseStart = min(node1, n - k) # Inclusive
#                 loNode2 = 2 * loReverseStart + k - 1 - node1
#                 hiNode2 = 2 * hiReverseStart + k - 1 - node1  # Inclusive
#                 # We will exclude the entire range from future iterations
#                 # by setting nextNode2s[node2] to hiNode2 + 2 for every
#                 # visited node2.
#                 postHiNode2 = hiNode2 + 2
#                 node2 = loNode2
#                 while node2 <= hiNode2:
#                     nextNode2 = nextNode2s[node2]
#                     nextNode2s[node2] = postHiNode2
#                     if node2 >= 0 and node2 < n and out[node2] == -1:
#                         newNodes.append(node2)
#                         out[node2] = depth
#                     node2 = nextNode2
#             nodes = newNodes
            
#         # Mark all banned positions as -1 (see above).
#         for i in range(n):
#             if out[i] == -2:
#                 out[i] = -1
#         return out
        






from sortedcontainers import SortedList
from collections import deque

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: list[int], k: int) -> list[int]:
        ans = [-1] * n
        ans[p] = 0
        banned_set = set(banned)
        
        # Two sorted lists: unvisited positions for even and odd indices
        unvisited = [SortedList(), SortedList()]
        for i in range(n):
            if i != p and i not in banned_set:
                unvisited[i % 2].add(i)
        
        queue = deque([p])
        
        while queue:
            cur = queue.popleft()
            # Compute the reachable range [lo, hi] with step 2
            lo = max(cur - k + 1, k - 1 - cur)
            hi = min(cur + k - 1, 2 * n - k - 1 - cur)
            
            parity = lo % 2
            sl = unvisited[parity]
            
            # Find all positions in [lo, hi] within the sorted list
            idx = sl.bisect_left(lo)
            to_remove = []
            while idx < len(sl) and sl[idx] <= hi:
                pos = sl[idx]
                to_remove.append(pos)
                ans[pos] = ans[cur] + 1
                queue.append(pos)
                idx += 1
            
            for pos in to_remove:
                sl.remove(pos)
        
        return ans

