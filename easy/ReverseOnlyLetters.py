'''
Problem URL: https://leetcode.com/problems/reverse-only-letters/description/?

Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

Example 1:
Input: s = "ab-cd"
Output: "dc-ba"

Example 2:
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Constraints:
1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.
'''

class Solution:
    # def reverseOnlyLetters(self, s: str) -> str:
    #     s = list(s)
    #     first = 0
    #     last = len(s) - 1
    #     while first < last:
    #         if s[first].isalpha() and s[last].isalpha():
    #             s[first], s[last] = s[last], s[first]
    #             first += 1
    #             last -= 1
    #         elif not s[first].isalpha():
    #             first += 1
    #         elif not s[last].isalpha():
    #             last -= 1
    #     return "".join(s)


    def isalphabetic(self,x):
        x= ord(x)
        if 65<=x<=90 or 97<=x<=122:
            return True
        return False
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        i = 0
        j = len(s)-1
        while i<j:
            if not self.isalphabetic(s[i]):
                i+=1
            elif not self.isalphabetic(s[j]):
                j-=1
            else:
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
        return "".join(s)