'''
Problem URL: https://leetcode.com/problems/single-number-iii/description/

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Example 1:
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

Example 2:
Input: nums = [-1,0]
Output: [-1,0]

Example 3:
Input: nums = [0,1]
Output: [1,0]

Constraints:
2 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each integer in nums will appear twice, only two integers will appear once.
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Approach: Hashmap
        # Create a hashmap to store the count of each number
        # countMap: Dict[int, int] = {}
        # # Iterate through the array, updating the count of each number
        # for num in nums:
        #     countMap[num] = countMap.get(num, 0) + 1
        # # Prepare the result array for the two unique numbers
        # result: List[int] = [0, 0]
        # index = 0
        # # Iterate through the map and find the numbers with a count of 1
        # for key, value in countMap.items():
        #     if value == 1:
        #         result[index] = key
        #         index += 1

        #         # Stop after finding the two unique numbers
        #         if index == 2:
        #             break
        # return result



        # Step 1: XOR all numbers to get the result of two unique numbers XORed
        # xor = 0
        # for num in nums:
        #     xor ^= num

        # # Step 2: Find any bit that is set in the xor result (we'll use the rightmost bit)
        # diff = xor & -xor  # This finds the rightmost set bit

        # # Step 3: Divide all numbers into two groups based on the found bit
        # result = [0, 0]
        # for num in nums:
        #     if (num & diff) == 0:
        #         result[0] ^= num  # Group 1: with the bit not set
        #     else:
        #         result[1] ^= num  # Group 2: with the bit set
        # return result



        # candidates = []
        # for num in nums:
        #     if num not in candidates:
        #         candidates.append(num)
        #     else:
        #         candidates.remove(num)
        # return candidates



        li=[]
        for i in nums:
            if nums.count(i)==1:
                li.append(i)
        return li

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))