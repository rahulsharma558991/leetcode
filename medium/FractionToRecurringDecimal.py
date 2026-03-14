'''
Problem URL: https://leetcode.com/problems/fraction-to-recurring-decimal/description

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses
If multiple answers are possible, return any of them.
It is guaranteed that the length of the answer string is less than 104 for all the given inputs.
Note that if the fraction can be represented as a finite length string, you must return it.

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:
Input: numerator = 2, denominator = 1
Output: "2"

Example 3:
Input: numerator = 4, denominator = 333
Output: "0.(012)"

Constraints:
-231 <= numerator, denominator <= 231 - 1
denominator != 0
'''

# class Solution:
#     def fractionToDecimal(self, numerator: int, denominator: int) -> str:
#         if numerator == 0:
#             return "0"

#         fraction = []
#         if (numerator < 0) ^ (denominator < 0):
#             fraction.append("-")

#         dividend = abs(numerator)
#         divisor = abs(denominator)
#         fraction.append(str(dividend // divisor))
#         remainder = dividend % divisor
#         if remainder == 0:
#             return "".join(fraction)

#         fraction.append(".")
#         map_dict = {}
#         while remainder != 0:
#             if remainder in map_dict:
#                 fraction.insert(map_dict[remainder], "(")
#                 fraction.append(")")
#                 break
#             map_dict[remainder] = len(fraction)
#             remainder *= 10
#             fraction.append(str(remainder // divisor))
#             remainder %= divisor

#         return "".join(fraction)






# class Solution:
#     def fractionToDecimal(self, numerator: int, denominator: int) -> str:
#         if numerator == 0: return "0"
        
#         res = []
#         # Handle sign
#         if (numerator < 0) ^ (denominator < 0):
#             res.append("-")
            
#         numerator, denominator = abs(numerator), abs(denominator)
        
#         # Integer part
#         res.append(str(numerator // denominator))
#         remainder = numerator % denominator
        
#         if remainder == 0:
#             return "".join(res)
            
#         res.append(".")
#         remainder_map = {}
        
#         # Fractional part
#         while remainder:
#             if remainder in remainder_map:
#                 res.insert(remainder_map[remainder], "(")
#                 res.append(")")
#                 break
            
#             remainder_map[remainder] = len(res)
#             remainder *= 10
#             res.append(str(remainder // denominator))
#             remainder %= denominator
            
#         return "".join(res)







# class Solution:
#     def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
#         if numerator % denominator == 0:
#             return str(numerator // denominator)
        
#         sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
        
#         numerator = abs(numerator)
#         denominator = abs(denominator)
        
#         integer = numerator // denominator
#         remainder = numerator % denominator
        
#         result = sign + str(integer) + "."
        
#         seen = {}
        
#         while remainder:
            
#             if remainder in seen:
#                 idx = seen[remainder]
#                 result = result[:idx] + "(" + result[idx:] + ")"
#                 return result
            
#             seen[remainder] = len(result)
            
#             remainder *= 10
            
#             result += str(remainder // denominator)
            
#             remainder %= denominator
        
#         return result









class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'

        x = numerator
        y = denominator
        neg = (x<0) ^ (y<0)

        x = -x if x <0 else x
        y = -y if y < 0 else y
        
        ans = ["-"] if neg else []
        if x < y:
            ans.append('0')
        while x >= y:
            ans.append(str(x//y))
            x %= y
        if x == 0:
            return ''.join(ans)
    
        ans.append('.')
        
        decimal = []
        seen = {}
        idx = 0
        while x != 0 :
            seen[x] = idx
            idx += 1
            
            x *= 10
            decimal.append(str(x//y))
            x %= y
            if x in seen:
                ans = ans + decimal[:seen[x]] +  ['('] + decimal[seen[x]:] + [')']
                break
        if x == 0:
            ans = ans + decimal
        
        
        return "".join(ans)