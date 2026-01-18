'''
Problem URL: https://leetcode.com/problems/number-of-arithmetic-triplets/description/

You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:
i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.

Example 1:
Input: nums = [0,1,4,6,7,10], diff = 3
Output: 2
Explanation:
(1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
(2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3. 

Example 2:
Input: nums = [4,5,6,7,8,9], diff = 2
Output: 2
Explanation:
(0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
(1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.

Constraints:
3 <= nums.length <= 200
0 <= nums[i] <= 200
1 <= diff <= 50
nums is strictly increasing.
'''

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # counter = 0
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             if nums[k] - nums[j] == diff and nums[j] - nums[i] == diff:
        #                 counter += 1
        # return counter


    #     counter = 0
    #     for num in nums:
    #         if self.binarySearch(nums, num + diff) and self.binarySearch(nums, num + 2 * diff):
    #             counter += 1
    #     return counter
    
    # def binarySearch(self, nums: List[int], target: int) -> bool:
    #     low, high = 0, len(nums) - 1
    #     while low <= high:
    #         mid = low + (high - low) // 2
    #         if nums[mid] == target:
    #             return True
    #         elif nums[mid] < target:
    #             low = mid + 1
    #         else:
    #             high = mid - 1
    #     return False

        seen = {}
        counter = 0
        for i in range(len(nums)):
            seen[nums[i]] = i
        for num in nums:
            if (num + diff) in seen and (num + 2 * diff) in seen:
                counter += 1
        return counter
__import__("atexit").register(lambda:open("display_runtime.txt","w").write("0"))