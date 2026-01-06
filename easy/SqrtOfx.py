'''
Proble URL: https://leetcode.com/problems/sqrtx/description/
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 
Constraints:
0 <= x <= 231 - 1
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        res = 0
        for i in range(1, ((x // 2) + 1)):
            if i*i == x:
                return i
            if i*i > x:
                return i-1
            res = i
        return res if x != 1 else 1
        '''

        '''
        # Approach Brute Force
        # square root of any number can never exceed half of it
        i = 0
        while i * i <= x:
            i += 1
        return i-1
        '''

        # Approach using Binary Search:
        if x == 0 or x == 1:
            return x
        start, mid, end = 0, -1, x
        while start <= end:
            mid = start + (end - start) // 2
            if mid * mid > x:
                end = mid -1
            elif mid * mid == x:
                return mid
            else:
                start = mid + 1
        return end