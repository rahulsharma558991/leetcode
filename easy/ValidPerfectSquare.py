'''
Problem URL: https://leetcode.com/problems/valid-perfect-square/description/

Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

Constraints:
1 <= num <= 231 - 1
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        '''
        # Approach Brute Force
        i = 1
        while i*i < num:
            i += 1
        return True if i*i <= num else False
        '''
        # Approach: Binary Search
        if num == 1:
            return True
        start, mid, end = 0, -1, num
        while start <= end:
            mid = start + (end - start) // 2
            if mid * mid > num:
                end = mid - 1
            elif mid * mid == num:
                return True
            else:
                start = mid + 1
            print("mid:", mid)
        return False