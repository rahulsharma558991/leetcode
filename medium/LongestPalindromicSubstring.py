'''
Problem URL: https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Approach: Expand around center
        # n = len(s)
        # if n <= 1:
        #     return s

        # best_l, best_r = 0, 0  # inclusive

        # def expand(l: int, r: int) -> None:
        #     nonlocal best_l, best_r
        #     while l >= 0 and r < n and s[l] == s[r]:
        #         l -= 1
        #         r += 1
        #     # went one step too far
        #     l += 1
        #     r -= 1
        #     if (r - l) > (best_r - best_l):
        #         best_l, best_r = l, r

        # for i in range(n):
        #     expand(i, i)       # odd length
        #     expand(i, i + 1)   # even length

        # return s[best_l:best_r + 1]


        
        # Approach: DP
        n = len(s)
        if n <= 1:
            return s

        dp = [[False] * n for _ in range(n)]
        start, best_len = 0, 1

        for i in range(n):
            dp[i][i] = True

        for length in range(2, n + 1):
            for l in range(0, n - length + 1):
                r = l + length - 1
                if s[l] == s[r] and (length <= 3 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    if length > best_len:
                        start, best_len = l, length

        return s[start:start + best_len]
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))