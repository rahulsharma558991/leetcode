'''
Problem URL: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/

You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.
Return true if you can make arr equal to target or false otherwise.

Example 1:
Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
Explanation: You can follow the next steps to convert arr to target:
1- Reverse subarray [2,4,1], arr becomes [1,4,2,3]
2- Reverse subarray [4,2], arr becomes [1,2,4,3]
3- Reverse subarray [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.

Example 2:
Input: target = [7], arr = [7]
Output: true
Explanation: arr is equal to target without any reverses.

Example 3:
Input: target = [3,7,9], arr = [3,7,11]
Output: false
Explanation: arr does not have value 9 and it can never be converted to target.

Constraints:
target.length == arr.length
1 <= target.length <= 1000
1 <= target[i] <= 1000
1 <= arr[i] <= 1000
'''

# class Solution:
#     def canBeEqual(self, targetArray: List[int], currentArray: List[int]) -> bool:
#         elementCounts = [0] * 1001
#         uniqueCount = 0
        
#         for t, c in zip(targetArray, currentArray):
#             if elementCounts[t] == 0:
#                 uniqueCount += 1
#             elementCounts[t] += 1
            
#             if elementCounts[c] == 1:
#                 uniqueCount -= 1
#             elementCounts[c] -= 1
        
#         return uniqueCount == 0










# class Solution:
#     MAX_VALUE = 1000
#     PRIMES = []

#     @classmethod
#     def generate_primes(cls, n):
#         primes = [0] * (n + 1)
#         primes[1] = 2  # Start with 2 as the first prime
#         count = 1
#         num = 3
#         while count < n:
#             if cls.is_prime(num):
#                 count += 1
#                 primes[count] = num
#             num += 2
#         return primes

#     @staticmethod
#     def is_prime(n):
#         if n < 2:
#             return False
#         if n == 2:
#             return True
#         if n % 2 == 0:
#             return False
#         for i in range(3, int(n**0.5) + 1, 2):
#             if n % i == 0:
#                 return False
#         return True

#     def canBeEqual(self, target, arr):
#         signature_target = 1
#         signature_arr = 1
#         for i in range(len(target)):
#             signature_target *= self.PRIMES[target[i]]
#             signature_arr *= self.PRIMES[arr[i]]
#         return signature_target == signature_arr

# # Initialize PRIMES
# Solution.PRIMES = Solution.generate_primes(Solution.MAX_VALUE)









# from collections import Counter

# class Solution:
#     def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
#         return Counter(target) == Counter(arr)








class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        from collections import Counter
        targetDict = Counter(target)
        arrDict = Counter(arr)
        if len(targetDict) != len(arrDict):
            return False
        for key, val in targetDict.items():
            if key not in arrDict or val != arrDict[key]:
                return False
        return True