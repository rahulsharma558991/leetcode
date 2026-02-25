'''
Problem URL: https://leetcode.com/problems/1-bit-and-2-bit-characters/description/

We have two special characters:
The first character can be represented by one bit 0.
The second character can be represented by two bits (10 or 11).
Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

Example 1:
Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.

Example 2:
Input: bits = [1,1,1,0]
Output: false
Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.

Constraints:
1 <= bits.length <= 1000
bits[i] is either 0 or 1.
'''

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # n = len(bits)
        # i = 0
        # while i < n - 1:
        #     i += bits[i] + 1
        # return i == n - 1



        # op = 0
        # bits = bits[::-1]
        # while bits:
        #     op = bits.pop()
        #     if op:
        #         bits.pop()
        # return not op




        # bits.pop()
        # n = len(bits)
        # if n == 0 or bits[-1] == 0:
        #     return True
        # ones = 0
        # for i in range(n - 1, -1, -1):
        #     if bits[i] == 1:
        #         ones += 1
        #     else:
        #         break
        # return not (ones & 1)




        # return re.sub('1, .','_',str(bits))[-2]=='0'




        i = 0
        n = len(bits)
        while i < n - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i == n - 1