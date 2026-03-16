'''
Problem URL: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         first, last = -1, -1
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 if first == -1:
#                     first = i
#                 last = i
#         return [first, last]






# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         if not nums:
#             return [-1, -1]

#         def find_first():
#             l, r = 0, len(nums) - 1
#             # [8]
#             # [8, 8]
#             # [7, 8, 8]
#             # [8, 8, 8]
#             # [6, 7, 8]
#             while l < r:
#                 mid = (l + r) // 2
#                 if nums[mid] < target:
#                     l = mid + 1
#                 elif nums[mid] > target:
#                     r = mid - 1
#                 elif nums[mid] == target:
#                     r = mid
#             return l if 0 <= l < len(nums) and nums[l] == target else -1

#         def find_last():
#             l, r = 0, len(nums) - 1
#             # [2, 2] target = 3
#             while l < r:
#                 mid = (l + r + 1) // 2
#                 if nums[mid] < target:
#                     l = mid + 1
#                 elif nums[mid] > target:
#                     r = mid - 1
#                 else:
#                     l = mid 
#             return l if 0 <= l < len(nums) and nums[l] == target else -1

#         s, e = find_first(), find_last()
#         return [s, e]








# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:         
    
#         def binary_search (nums, target, is_searching_left):
#             l, r, idx = 0, len(nums) - 1, -1
#             while l <= r: 
#                 mid = (l + r) // 2
#                 if nums[mid] < target: 
#                     l = mid + 1
#                 elif nums[mid] > target: 
#                     r = mid - 1
#                 else: 
#                     idx = mid
#                     if is_searching_left: 
#                         r = mid - 1
#                     else: 
#                         l = mid + 1            
#             return idx
        
#         left = binary_search(nums, target, True)
#         right = binary_search(nums, target, False)

#         return [left, right]

# # 5, 7, 8, 8, 8, 8, 10



















class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]
        def bisect_left(arr, target):
            left = 0
            right = len(arr) - 1
            mid = (left + right) // 2
            while True:
                # print(left, right, mid)
                if left == right:
                    return left if arr[left] == target else -1
                if left == right - 1:
                    if arr[left] == target:
                        return left
                    if arr[right] == target:
                        return right
                    else:
                        return -1
                if arr[mid] < target:
                    left = mid + 1
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    right = mid
                mid = (left + right) // 2
        def bisect_right(arr, target):
            left = 0
            right = len(arr) - 1
            mid = (left + right) // 2
            while True:
                if left == right:
                    return left if arr[left] == target else -1
                if left == right - 1:
                    if arr[right] == target:
                        return right
                    if arr[left] == target:
                        return left
                    else:
                        return -1
                if arr[mid] < target:
                    left = mid + 1
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid
                mid = (left + right) // 2
        return [bisect_left(nums, target), bisect_right(nums, target)]