'''
Problem URL: https://leetcode.com/problems/reverse-prefix-of-word/description/

Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.
For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
Return the resulting string.

Example 1:
Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3. 
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

Example 2:
Input: word = "xyxzxe", ch = "z"
Output: "zxyxxe"
Explanation: The first and only occurrence of "z" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".

Example 3:
Input: word = "abcd", ch = "z"
Output: "abcd"
Explanation: "z" does not exist in word.
You should not do any reverse operation, the resulting string is "abcd".

Constraints:
1 <= word.length <= 250
word consists of lowercase English letters.
ch is a lowercase English letter.
'''

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # idx = 0
        # ans = ""
        # for i in range(len(word)):
        #     if word[i] == ch:
        #         idx = i
        #         break
        # for j in range(idx, -1, -1):
        #     ans += word[j]
        # for k in range(idx + 1, len(word)):
        #     ans += word[k]
        # return ans








        # if len(word) == 1:
        #     return word

        # left, right, found, res = 0, 0, False, [''] * len(word)

        # for i in range(len(word)):
        #     res[i] = word[i]
        #     if (word[i] == ch and not found):
        #         found = True
        #         right = i

        # while left < right:
        #     res[left], res[right] = res[right], res[left]
        #     left += 1
        #     right -= 1

        # return ''.join(res)







        # res = ""
        # found = False
        # for val in word:
        #     if not found:
        #         res = val + res
        #     else:
        #         res += val
        #     if val == ch:
        #         found = True
        # if not found :
        #     return word
        # return res









        # ind = None
        # for i, c in enumerate(word):
        #     if c == ch:
        #         ind = i
        #         break
        
        # if not ind:
        #     return word

        # res = []
        # i = ind
        # while i >= 0:
        #     res.append(word[i])
        #     i -= 1
        
        # for i in range(ind + 1, len(word)):
        #     res.append(word[i])

        # return "".join(res)








        """
        Notes:
        - input: string word, character ch
        - output: reverse word that starts at index 0 and ends at first occurence of ch
        """
        word_arr = list(word)
        result_arr = []
        for i in range(len(word)):
            # append the currect character
            result_arr.append(word_arr[i])
            if word_arr[i] == ch:
                result_arr = result_arr[::-1]
                # add the rest of the characters in word and return the string
                for j in range(i + 1, len(word)):
                    result_arr.append(word_arr[j])
                return "".join(result_arr)

        return word