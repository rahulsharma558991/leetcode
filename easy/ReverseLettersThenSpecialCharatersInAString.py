'''
Problem URL: https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/description/

You are given a string s consisting of lowercase English letters and special characters.
Your task is to perform these in order:

Reverse the lowercase letters and place them back into the positions originally occupied by letters.
Reverse the special characters and place them back into the positions originally occupied by special characters.
Return the resulting string after performing the reversals.

Example 1:
Input: s = ")ebc#da@f("
Output: "(fad@cb#e)"
Explanation:
The letters in the string are ['e', 'b', 'c', 'd', 'a', 'f']:
Reversing them gives ['f', 'a', 'd', 'c', 'b', 'e']
s becomes ")fad#cb@e("
​​​​​​​The special characters in the string are [')', '#', '@', '(']:
Reversing them gives ['(', '@', '#', ')']
s becomes "(fad@cb#e)"

Example 2:
Input: s = "z"
Output: "z"
Explanation:
The string contains only one letter, and reversing it does not change the string. There are no special characters.

Example 3:
Input: s = "!@#$%^&*()"
Output: ")(*&^%$#@!"
Explanation:
The string contains no letters. The string contains all special characters, so reversing the special characters reverses the whole string.

Constraints:
1 <= s.length <= 100
s consists only of lowercase English letters and the special characters in "!@#$%^&*()".
'''

class Solution:
    def reverseByType(self, s: str) -> str:
        # s = list(s)
        # alphalist = []
        # specialCharlist = []
        # for index, char in enumerate(s):
        #     if char.isalpha():
        #         alphalist.append(char)
        #     else:
        #         specialCharlist.append(char)
        # alphalist = alphalist[::-1]
        # specialCharlist = specialCharlist[::-1]
        # alphaIndex = 0
        # specialCharIndex = 0
        # for index, char in enumerate(s):
        #     if char.isalpha():
        #         s[index] = alphalist[alphaIndex]
        #         alphaIndex += 1
        #     else:
        #         s[index] = specialCharlist[specialCharIndex]
        #         specialCharIndex += 1
        # return "".join(s)






        # alphabet = string.ascii_lowercase
        # letters = [c for c in s if c in alphabet]
        # special_chars = [c for c in s if c not in alphabet]
        # new_str = [] 
        # for i in range(len(s)): 
        #     if s[i] in alphabet: 
        #         new_char = letters.pop()
        #     else:
        #         new_char = special_chars.pop()
                
        #     new_str.append(new_char)
        # assert not letters and not special_chars 
        # new_str = "".join(new_str)
        # assert len(new_str) == len(s)
        # return new_str






        letters = []
        specials = []
        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            else:
                specials.append(ch)
        letters = letters[::-1]
        specials = specials[::-1]
        result = ""
        i = j = 0
        for ch in s:
            if ch.isalpha():
                result += letters[i]
                i += 1
            else:
                result += specials[j]
                j += 1
        return result
