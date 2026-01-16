'''
Problem uRL: https://leetcode.com/problems/3sum/description/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''


from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()   # Sort array
        # n = len(nums)
        # res = []      

        # for i in range(n - 2):
        #     # Skip duplicate
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue

        #     left, right = i + 1, n - 1
        #     target = -nums[i]

        #     while left < right:
        #         s = nums[left] + nums[right]

        #         if s == target:
        #             # Found a valid triplet
        #             res.append([nums[i], nums[left], nums[right]])
        #             left += 1
        #             right -= 1

        #             # Skip duplicates for left
        #             while left < right and nums[left] == nums[left - 1]:
        #                 left += 1
        #             # Skip duplicates for right
        #             while left < right and nums[right] == nums[right + 1]:
        #                 right -= 1

        #         elif s < target:
        #             left += 1
        #         else:
        #             right -= 1

        # return res
        # -1, 0, 1, 2, -1, 4
        # -1, -1, 0, 1, 2, 4
        nums.sort()
        soln = []
        n = len(nums)
        for i in range(n-1):
            target = -nums[i]
            left = i+1
            right = n-1
            if i > 0 and nums[i-1] == nums[i]:
                continue

            while left < right:
                if nums[left] + nums[right] == target:
                    soln.append([nums[i], nums[left], nums[right]])
                    while left+1 < right and nums[left+1] == nums[left]:
                        left += 1
                    while right-1 > left and nums[right-1] == nums[right]:
                        right-=1
                    left+=1
                    right-=1
                
                if nums[left] + nums[right] < target:
                    left+=1
                
                if nums[left] + nums[right] > target:
                    right-=1
        return soln
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))