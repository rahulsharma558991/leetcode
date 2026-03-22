'''
Problem URL: https://leetcode.com/problems/reverse-pairs/description/

Given an integer array nums, return the number of reverse pairs in the array.
A reverse pair is a pair (i, j) where:
0 <= i < j < nums.length and
nums[i] > 2 * nums[j].

Example 1:
Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1

Example 2:
Input: nums = [2,4,3,5,1]
Output: 3
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1

Constraints:
1 <= nums.length <= 5 * 104
-231 <= nums[i] <= 231 - 1
'''

# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
#         # Approach: 2 for loops TLE
#         # count = 0
#         # n = len(nums)
#         # for i in range(0, n-1):
#         #     for j in range(i+1, n):
#         #         if nums[i] > 2*nums[j]:
#         #             count += 1
#         # return count





#         seen = SortedList()
#         ans = 0
#         for x in reversed(nums):
#             ans += seen.bisect_left(x / 2)
#             seen.add(x)
#         return ans






class Solution:
    def merge(self, nums, low, mid, high):
        temp = []
        left = low
        right = mid+1
        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                right+=1
        while left <= mid:
            temp.append(nums[left])
            left+=1
        while right <= high:
            temp.append(nums[right])
            right+=1

        nums[low:high+1] = temp
    
    def count(self, nums, low, mid, high):
        cnt = 0
        right = mid+1
        for i in range(low,mid+1):
            while right <= high and nums[i] > 2*nums[right]:
                right+=1
            cnt += right-(mid+1)

        return cnt
        
    def mergeSort(self, nums, low, high):
        ans = 0
        if low >= high:
            return ans
        mid = (low + high)//2
        ans += self.mergeSort(nums, low, mid)
        ans += self.mergeSort(nums, mid+1, high)
        ans += self.count(nums, low, mid, high)
        self.merge(nums, low, mid, high)
        return ans

    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums)-1)
        