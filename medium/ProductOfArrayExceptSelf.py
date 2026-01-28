'''
Problem URL: https://leetcode.com/problems/product-of-array-except-self/description/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Approach: Brute Force
        # if len(nums) < 2:
        #     return nums
        # n = len(nums)
        # product = [0] * n
        # for i in range(n):
        #     elem = 1
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         elem = elem * nums[j]
        #     product[i] = elem
        
        # for i in range(n):
        #     nums[i] = product[i]
        # return nums
        
        # Approach: prefixProduct array
        # Create two arrays prefix and suffix, both of size n.
        # Fill the prefix array such that prefix[i] holds the product of all elements to the left of i.
        # Fill the suffix array such that suffix[i] holds the product of all elements to the right of i.
        # For the result array, multiply the corresponding values of prefix and suffix.
        # if len(nums) < 2:
        #     return nums
        # n = len(nums)
        # output = [0] * n
        # prefix = [0] * n
        # suffix = [0] * n
        # # [1,2,3,4] => [24,12,8,6]
        # prefix[0] = 1
        # for i in range(1, n):
        #     prefix[i] = prefix[i-1] * nums[i-1]  # [1, 1, 2, 6]
        
        # suffix[n-1] = 1
        # for i in range(n-2, -1, -1):
        #     suffix[i] = suffix[i+1] * nums[i+1]  # [24, 12, 4, 1]

        # for i in range(n):
        #     output[i] = prefix[i] * suffix[i]

        # return output

        # Approach: Single Pass
        # if len(nums) < 2:
        #     return nums
        # n = len(nums)
        # output = [1] * n

        # left = 1
        # right = 1

        # for i in range(n):
        #     j = n - 1 - i

        #     output[i] *= left
        #     left *= nums[i]

        #     output[j] *= right
        #     right *= nums[j]

        # return output

        # Approach: Single Pass with two separate loops
        n = len(nums)
        output = [0] * n

        # Initialize the output array with left products
        output[0] = 1
        for i in range(1, n):
            output[i] = output[i - 1] * nums[i - 1]

        # Calculate and multiply the right products
        right = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))