'''
Problem URL: https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/

Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

Example 1:
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Example 2:
Input: nums = [-1]
Output: [0]

Example 3:
Input: nums = [-1,-1]
Output: [0,0]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
'''

# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:
#         result = []
#         sorted_nums = []
        
#         # Process from right to left ⬅️
#         for num in reversed(nums):
#             # Find insertion position using binary search 🔍
#             insert_pos = bisect.bisect_left(sorted_nums, num)
#             result.append(insert_pos)
#             # Insert into the sorted list to maintain order
#             bisect.insort(sorted_nums, num)
        
#         # Reverse to get the correct order 🔄
#         return result[::-1]




# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:

#         n = len(nums)
#         values = sorted(nums)
#         index = {v: i for i, v in enumerate(values)}
#         count = [0] * n
#         st = SegmentTree(n)

#         for i in range(n - 1, -1, -1):
#             left = 0
#             right = index[nums[i]] - 1  # query strictly smaller int
#             count[i] = st.query(left, right)
#             st.update(index[nums[i]])

#         return count

# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))    


# class SegmentTree:

#     def __init__(self, size):
#         self.n = size
#         self.tree = [0] * (4 * size)

#     def query(self, left, right):
#         return self._query(1, 0, self.n - 1, left, right)

#     def _query(self, node, left, right, ql, qr):
#         if ql > right or qr < left:
#             return 0

#         if ql <= left and right <= qr:
#             return self.tree[node]

#         mid = left + (right - left) // 2
#         left_sum = self._query(node * 2, left, mid, ql, qr)
#         right_sum = self._query(node * 2 + 1, mid + 1, right, ql, qr)
#         return left_sum + right_sum

#     def update(self, idx):
#         self._update(1, 0, self.n - 1, idx)

#     def _update(self, node, left, right, idx):
#         if left == right:
#             self.tree[node] += 1
#             return

#         mid = left + (right - left) // 2
#         if idx <= mid:
#             self._update(node * 2, left, mid, idx)
#         else:
#             self._update(node * 2 + 1, mid + 1, right, idx)

#         self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]







# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:
#         unique = sorted(set(nums))
#         memo = {v: i + 1 for i, v in enumerate(unique)}
#         n = len(unique)
#         tree = [0] * (n + 1)
#         res = [0] * len(nums)
#         for i in range(len(nums) - 1, -1, -1):
#             t = memo[nums[i]]
#             k = t - 1
#             while t < n:
#                 tree[t] += 1
#                 t += t & -t
#             ans = 0
#             while k != 0:
#                 ans += tree[k]
#                 k -= k & -k
#             res[i] = ans
#         return res







# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:
#         #given nums return counts
#         #counts[i] is smaller elements to right of nums[i]
#         #go through from r to l, keep a prefix sum array
#         #then binary search on this array, add 1 to next smallest number

#         prefix = SortedList()
#         ans = []
#         for n in reversed(nums):
#             i = prefix.bisect_left(n) 
#             ans.append(i)   
#             prefix.add(n)
#         ans.reverse()
#         return ans





# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:
#         N = len(nums)
#         res = [0] * N
#         enum_nums = list(enumerate(nums))
#         def merge_sort(arr):
#             if len(arr) <= 1:
#                 return arr
#             mid = len(arr) // 2
#             left = merge_sort(arr[:mid])
#             right = merge_sort(arr[mid:])
#             return merge(left, right)
#         def merge(left, right):
#             sorted_arr = []
#             i = j = 0
#             right_count = 0
#             while i < len(left) and j < len(right):
#                 if left[i][1] > right[j][1]:
#                     right_count += 1
#                     sorted_arr.append(right[j])
#                     j += 1
#                 else:
#                     res[left[i][0]] += right_count
#                     sorted_arr.append(left[i])
#                     i += 1
#             while i < len(left):
#                 res[left[i][0]] += right_count
#                 sorted_arr.append(left[i])
#                 i += 1
#             while j < len(right):
#                 sorted_arr.append(right[j])
#                 j += 1
#             return sorted_arr
#         merge_sort(enum_nums)
#         return res






class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def binary_search(arr,x):
            l, r = 0, len(arr)
            while l < r:
                mid = (l+r) //2
                if arr[mid] < x:
                    l = mid + 1
                else:
                    r = mid
            return l

        sorted_seen = [] #store the sorted num, how many number less than will be that index
        n = len(nums)
        res = [0] * n

        for i in range(n-1,-1,-1):
            pos = binary_search(sorted_seen, nums[i])
            res[i] = pos
            sorted_seen.insert(pos, nums[i])

        return res