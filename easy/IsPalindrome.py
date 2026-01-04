'''
URL : https://leetcode.com/problems/palindrome-number/description/
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        # string conversion code
        str_x = str(x)
        return True if str_x == str_x[::-1] else False
        '''
        # without string conversion code
        temp = x
        rev = 0
        while temp > 0:
            rem = temp % 10
            temp = temp // 10
            rev = rev * 10 + rem
        return True if rev == x else False 
