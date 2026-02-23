'''
Problem URL: https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.
A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

Example 1:
Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.

Example 2:
Input: nums = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.

Constraints:
1 <= nums.length <= 104
-109 <= nums[i] <= 109
'''

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # long = 1
        # currLen = 1
        # for i in range(1, n):
        #     if nums[i] > nums[i - 1]:
        #         currLen += 1
        #         long = max(long, currLen)
        #     else:
        #         currLen = 1
        # return long




        # count = 1
        # best = 1

        # for i in range(len(nums)-1):
        #     if nums[i + 1] > nums[i]:
        #         count += 1
        #     else:
        #         count = 1
        #     if count > best:
        #         best = count
        # return best





        # if not nums:
        #     return 0
        # max_len=1
        # curr_len=1
        # for i in range(1,len(nums)):
        #     if nums[i] > nums[i-1]:
        #         curr_len+=1
        #     else:
        #         max_len=max(max_len,curr_len)
        #         curr_len=1
        # return max(max_len,curr_len)





#         if not nums:
#             return 0

#         current = 1
#         max_len = 1

#         for i in range(1, len(nums)):
#             if nums[i] > nums[i - 1]:
#                 current += 1
#             else:
#                 current = 1
#             max_len = max(max_len, current)

#         return max_len


# nums = [1, 3, 5, 4, 7]
# sol = Solution()
# print(sol.findLengthOfLCIS(nums))




        """
        Use two pointers to track the current subsequence. The key insight is
        that a continuous increasing subsequence can only break where the next
        element isn't larger, so resetting the left pointer at each break is
        sufficient - no backtracking needed.

        Time complexity: O(n), where n is the length of nums.
        Space complexity: O(1)
        """
        if len(nums) == 0:
            return 0

        longest_length = 1
        left = 0

        for right in range(1, len(nums)):
            if nums[right - 1] >= nums[right]:
                left = right
            else:
                longest_length = max(longest_length, right - left + 1)

        return longest_length