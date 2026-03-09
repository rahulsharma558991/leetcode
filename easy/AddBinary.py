'''
Problem URL: https://leetcode.com/problems/add-binary/description

Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # x, y = int(a, 2), int(b, 2)
        # while y:
        #     x, y = x ^ y, (x & y) << 1
        # return bin(x)[2:]




        # i, j = len(a)-1, len(b)-1
        # carry = 0
        # res = ""
        # while i >= 0 or j >= 0 or carry:
        #     carry+=(int(a[i]) if i>=0 else 0)
        #     carry+=(int(b[j]) if j>=0 else 0)
        #     res = str(carry % 2) + res
        #     carry //=2
        #     i-=1
        #     j-=1
        # return res





        # carry  = 0
        # i, j = len(a)-1, len(b)-1
        # res= []
        # while i>= 0 or j >= 0 or carry:
        #     s = carry
        #     if i >= 0:
        #         s += int(a[i])
        #         i -= 1
        #     if j >= 0:
        #         s += int(b[j])
        #         j -= 1
        #     res.append(str(s%2))
        #     carry = s//2
        # return "".join(reversed(res))






        # if a=="0" and b=="0":return "0"
        # lea=len(a)
        # leb=len(b)
        # c=0
        # l=[]
        # s=""
        # for i in range(lea):
        #     c+=int(a[i])*2**(lea-i-1)
        # for j in range(leb):
        #     c+=int(b[j])*2**(leb-j-1)
        # while c!=0:
        #     l.append(c%2)
        #     c=c//2
        # n=len(l)
        # l.reverse()
        # for k in range(n):
        #     s+=str(l[k])
        # return s

        # one liner solution by chatgpt
        return bin(int(a,2)+int(b,2))[2:]