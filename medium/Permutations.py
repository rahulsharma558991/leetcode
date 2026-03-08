'''
Problem URL: https://leetcode.com/problems/permutations/description/

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # def perms(i):
        #     if i == len(nums):
        #         res.append(nums[:])
        #         return
        #     for j in range(i, len(nums)):
        #         nums[i], nums[j] = nums[j], nums[i]
        #         perms(i + 1)
        #         nums[i], nums[j] = nums[j], nums[i]
        # perms(0)
        # return res




        # soln = []
        # cur = set()
        # curArr = []
        # def dfs(idx):
        #     cur.add(idx)
        #     curArr.append(nums[idx])
        #     # print(cur)
        #     if len(cur)==len(nums):
        #         soln.append(curArr.copy())
        #     else:
        #         for i in range(len(nums)):
        #             if i not in cur:
        #                 dfs(i)
        #     cur.remove(idx)
        #     curArr.pop()
        # for i,v in enumerate(nums):
        #     dfs(i)
        # return soln






        ans = []
        n = len(nums)
        def backtrack(cur: List[int]):
            nonlocal ans 
            if len(cur) == n: 
                ans.append(list(cur))
            else:
                for num in nums: 
                    if num not in cur: 
                        cur.append(num)
                        backtrack(cur)
                        cur.pop()
        backtrack([])
        return ans






        # res = []
        # def rec(idx):
        #     if idx == len(nums):
        #         res.append(nums.copy())
        #         return
        #     for i in range(idx, len(nums)):
        #         nums[idx], nums[i] = nums[i], nums[idx]
        #         rec(idx+1)
        #         nums[idx], nums[i] = nums[i], nums[idx]
        # rec(0)
        # return res






        used = [False] * len(nums)
        res = []
        def backtrack(sofar, length):
            if length == len(nums):
                res.append(sofar.copy())
                return
            for idx, val in enumerate(used):
                if not val:
                    used[idx] = True
                    sofar.append(nums[idx])
                    backtrack(sofar, length + 1)
                    used[idx] = False
                    sofar.pop()
        backtrack([], 0)
        return res