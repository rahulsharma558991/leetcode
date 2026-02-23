'''
Problem URL: https://leetcode.com/problems/count-of-range-sum/description/

Given an integer array nums and two integers lower and upper, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j inclusive, where i <= j.

Example 1:
Input: nums = [-2,5,-1], lower = -2, upper = 2
Output: 3
Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.

Example 2:
Input: nums = [0], lower = 0, upper = 0
Output: 1

Constraints:
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
-105 <= lower <= upper <= 105
The answer is guaranteed to fit in a 32-bit integer.
'''

# class Solution:
#     """My original solution without using packages"""
#     def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
#         res = 0
#         prefix = [0]
#         curr = 0

#         for num in nums:
#             curr += num
#             res += self.binary_search_high(prefix, curr - lower) - self.binary_search_low(prefix, curr - upper)
#             insert_index = self.binary_search_high(prefix, curr)
#             prefix.insert(insert_index, curr)
#         return res

#     def binary_search_high(self, arr, target):
#         left, right = 0, len(arr)
#         while left < right:
#             mid = (right + left) // 2
#             if arr[mid] <= target:
#                 left = mid + 1
#             else:
#                 right = mid
#         return left

#     def binary_search_low(self, arr, target):
#         left, right = 0, len(arr)
#         while left < right:
#             mid = (right + left) // 2
#             if arr[mid] < target: # This the the only difference
#                 left = mid + 1
#             else:
#                 right = mid
#         return left










# from sortedcontainers import SortedList
# class Solution:
#     """My solution with package"""
#     def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
#         res = 0
#         prefix = SortedList([0])
#         curr = 0
#         for num in nums:
#             curr += num
#             res += prefix.bisect_right(curr - lower) - prefix.bisect_left(curr-upper)
#             prefix.add(curr)
#         return res








# TLE
class Solution:
    """Sliding window is actually my first thought of this question, 
for anyone interested, this is kind of the sliding window/ O(n^2) linear solution."""
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            curr = 0
            for right in range(i, n):
                curr += nums[right]
                if lower <= curr <= upper:
                    res += 1
        return res