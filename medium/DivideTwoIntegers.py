'''
Problem URL: https://leetcode.com/problems/divide-two-integers/description

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
Return the quotient after dividing dividend by divisor.
Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Constraints:
-231 <= dividend, divisor <= 231 - 1
divisor != 0
'''

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # if dividend == divisor:
        #     return 1
        # if dividend == -2**31 and divisor == -1:
        #     return (2**31) - 1 
        
        # if divisor == 1:
        #     return dividend
        
        # sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        # n, d = abs(dividend), abs(divisor)
        # ans = 0

        # while n >= d:
        #     p = 0
        #     while n >= (d << p):
        #         p += 1
            
        #     p -= 1
        #     n -= (d << p)
        #     ans += (1 << p)

        # return min(max(sign * ans, -2**31), 2**31 - 1)





        # if dividend == divisor: return 1
        # sign = True
        # MAX_INT = (2**31) - 1
        # MIN_INT = -2**31
        # if dividend >= 0 and divisor < 0: sign = False
        # if dividend <= 0 and divisor > 0: sign = False

        # n = abs(dividend)
        # d = abs(divisor)
        # ans = 0

        # while n >= d:
        #     count = 0
        #     while (n >= (d << count + 1)):
        #         count += 1
        #     ans += 1 << count
        #     n -= (d << count)

        # res = ans if sign else -ans

        # if res >= MAX_INT:
        #     return MAX_INT

        # if ans < MIN_INT:
        #     return MIN_INT

        # return res







        # # 32-bit limits
        # INT_MIN = -2**31
        # INT_MAX = 2**31 - 1
        
        # # Special overflow case
        # if dividend == INT_MIN and divisor == -1:
        #     return INT_MAX
        
        # # Determine sign
        # negative = (dividend < 0) != (divisor < 0)
        
        # # Work with positive numbers
        # dividend = abs(dividend)
        # divisor = abs(divisor)
        
        # quotient = 0
        
        # # Main logic
        # while dividend >= divisor:
        #     temp = divisor
        #     multiple = 1
            
        #     while dividend >= (temp << 1):
        #         temp <<= 1
        #         multiple <<= 1
            
        #     dividend -= temp
        #     quotient += multiple
        
        # return -quotient if negative else quotient








        # 1. Handle the 32-bit integer overflow edge case
        # (Only happens when -2^31 is divided by -1)
        MAX_INT = 2147483647  # 2^31 - 1
        MIN_INT = -2147483648 # -2^31
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        # 2. Determine the sign using XOR
        negative = (dividend < 0) ^ (divisor < 0)
        
        # 3. Work with absolute values to simplify logic
        a, b = abs(dividend), abs(divisor)
        res = 0
        
        # 4. Exponential subtraction (Bit Shifting)
        # We try to fit the largest possible multiple of 'b' into 'a'
        for i in range(31, -1, -1):
            if (a >> i) >= b:    # Equivalent to: if a >= (b * 2^i)
                res += (1 << i)  # Add 2^i to the result
                a -= (b << i)    # Subtract (b * 2^i) from dividend
        
        # 5. Apply the sign and return
        return -res if negative else res