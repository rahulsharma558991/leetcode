'''
Problem URL: https://leetcode.com/problems/word-break/description

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # n = len(s)
        # dp = [False] * (n + 1)
        # dp[0] = True
        # max_len = max(map(len, wordDict))  # The maximum length of a word in the dictionary

        # for i in range(1, n + 1):
        #     for j in range(i - 1, max(i - max_len - 1, -1), -1): # Only consider words that could fit
        #         if dp[j] and s[j:i] in wordDict:
        #             dp[i] = True
        #             break

        # return dp[n]






        # Idea 1 - O(n*3) - n^2 substrings 
        # dp[i] = any(dp[j] and s[i:j] in wordSet for j in [i+1..n])
        # Idea 2 - Exponential T(i) = 2T(i+1) + O(n-i)
        # dp[i] = any(dp[j] word in  that dp[i:j] is in wordDict for j that [i:j] is the word length)


        # # Brute force
        # n = len(s)
        # def dfs(i):
        #     if i == n:
        #         return True
        #     for word in wordDict:
        #         j =  i + len(word)
        #         if s[i : j] == word and dfs(j):
        #             return True
        #     return False
        
        # return dfs(0)

        # # 1D top down dfs - O(nmk) time where m is the len of wordDict and k is the average len of the words. O(n) space
        # # 2:27 - 2:37
        # n = len(s)
        # memo = [None] * n
        # def dfs(i):
        #     if i == n:
        #         return True
        #     if memo[i] is not None:
        #         return memo[i]
        #     for word in wordDict:
        #         j =  i + len(word)
        #         # Becare we only return when both condition meets. Not to return dfs(j) when s[i:j] == word
        #         if s[i : j] == word and dfs(j):
        #             memo[i] = True
        #             return memo[i]
        #     memo[i] = False
        #     return memo[i]
        
        # return dfs(0)


        # Looping words 1D bottom up - O(nml) where m is the len of wordDict and l is the max len of the word in words. O(n) space
        # n = len(s)
        # dp = [False] * (n + 1)
        # dp[n] = True
        # for i in range(n - 1, -1, -1):
        #     for word in wordDict:
        #         j =  i + len(word)
        #         if j <= n and s[i : j] == word and dp[j]:
        #             dp[i] = True
        #             break

        # return dp[0] 


        # Looping index 1D bottom up - O(n^3) where k is the average len of the words. O(n) space
        #  dp[i] = any(dp[j] and s[i:j] in wordSet for j in [i+1..n])
        n = len(s)
        wordSet = set(wordDict)
        dp = [False] * (n + 1)
        dp[n] = True
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                if s[i : j] in wordSet and dp[j]:
                    dp[i] = True
                    break
        return dp[0]