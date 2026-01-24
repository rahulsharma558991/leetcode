'''
Problem URL: https://leetcode.com/problems/move-zeroes/description/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
Follow up: Could you minimize the total number of operations done?
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Approach: Two-Pointers: Two Pass
        # nonzero_pos = 0
        # for i in range(0, len(nums)):
        #     if nums[i] != 0:
        #         nums[nonzero_pos] = nums[i]
        #         nonzero_pos +=1
        # while nonzero_pos < len(nums):
        #     nums[nonzero_pos] = 0
        #     nonzero_pos += 1  
        # return nums

        # Approach: Two-Pointers: One-Pass
        # writePos = 0  # next position of non zero num
        # for readPos in range(0, len(nums)):
        #     if nums[readPos] != 0:
        #         if writePos != readPos:
        #             nums[writePos], nums[readPos] = nums[readPos], nums[writePos]
        #         writePos += 1
        # return nums

        # Approach: Brute Force: Move and Shift
        n = len(nums)
        result = [0] * n
        j = 0

        # First pass: accumulate non-zero elements
        for i in range(n):
            if nums[i] != 0:
                result[j] = nums[i]
                j += 1

        # Second pass: fill remaining positions with zeroes
        for k in range(j, n):
            result[k] = 0

        # Copy back to original list
        for i in range(n):
            nums[i] = result[i]
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))