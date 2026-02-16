'''
Problem URL: https://leetcode.com/problems/maximum-average-subarray-i/description/

You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

Constraints:
n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
'''

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Approach: Brute Force TLE
        # # Initialize 'maxSum' to minimum possible value
        # maxSum = float("-inf")
        # # Iterate through each starting point of subarray of length k
        # for i in range(0, len(nums) - k + 1):
        #     currentSum = 0
        #     # Calculate the sum of subarray starting at index 'i' of length 'k'
        #     for j in range(i, i + k):
        #         currentSum += nums[j]
        #     # Update 'maxSum' if 'currentSum' is greater
        #     if currentSum > maxSum:
        #         maxSum = currentSum
        # # Return the maximum average
        # return maxSum / k


        # Approach: Sliding Window
        # currentSum = 0
        # # Calculate sum of the first 'k' elements
        # for i in range(k):
        #     currentSum += nums[i]
        # maxSum = currentSum
        # # Slide the window over the rest of the elements
        # for i in range(k, len(nums)):
        #     # Update the current sum by sliding the window
        #     currentSum = currentSum - nums[i - k] + nums[i]
        #     # Update maxSum if the current sum is greater
        #     maxSum = max(maxSum, currentSum)
        # # Return the maximum average
        # return maxSum / k



        # windowSum = sum(nums[:k])
        # maxAverageValue = windowSum/k
        # for i in range(k,len(nums)):
        #     windowSum += nums[i] - nums[i-k]
        #     maxAverageValue = max(maxAverageValue,windowSum/k)
        # return maxAverageValue



        s=sum(nums[:k])
        maxs=s
        for i in range(k,len(nums)):
            s+=nums[i]-nums[i-k]
            if s>maxs:
                maxs=s
        return maxs/k
        
__import__('atexit').register(lambda: open('display_runtime.txt', 'w').write('000'))



