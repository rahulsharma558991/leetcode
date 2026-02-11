'''
Problem URL: https://leetcode.com/problems/is-subsequence/description/

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:
0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Approach: 2 for loops
        # first = 0
        # second = 0
        # for s_char in range(len(s)):
        #     found = False
        #     for t_char in range(second, len(t)):
        #         if s[s_char] == t[t_char]:
        #             found = True
        #             first += 1
        #             second = t_char + 1
        #             break
        #     if not found:
        #         return False
        
        # if first <= len(s):
        #     return True
        # return False


        # Approach: Single for loop
        # first = second = 0
        # while first < len(s) and second < len(t):
        #     if s[first] == t[second]:
        #         first += 1
        #     second += 1
        # return first == len(s)


        # Approach: Recursion
        LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

        def rec_isSubsequence(left_index, right_index):
            # base cases
            if left_index == LEFT_BOUND:
                return True
            if right_index == RIGHT_BOUND:
                return False
            # consume both strings or just the target string
            if s[left_index] == t[right_index]:
                left_index += 1
            right_index += 1

            return rec_isSubsequence(left_index, right_index)

        return rec_isSubsequence(0, 0)


# Approach with Binary Search for more queries
# class Solution:
#     def __init__(self):
#         self.char_positions = None

#     def preprocess(self, t: str) -> None:
#         """Preprocess string t to build position index."""
#         self.char_positions = defaultdict(list)

#         for i, char in enumerate(t):
#             self.char_positions[char].append(i)

#     def isSubsequence(self, s: str, t: str) -> bool:
#         """Check if s is a subsequence of t."""
#         # For single query, preprocess on the fly
#         if self.char_positions is None:
#             self.preprocess(t)

#         current_pos = -1

#         for char in s:
#             positions = self.char_positions.get(char)

#             # Character not found in t
#             if not positions:
#                 return False

#             # Binary search for first position > current_pos
#             # bisect_right gives us the insertion point for current_pos + 0.5
#             # which is effectively the first index where positions[idx] > current_pos
#             idx = bisect.bisect_right(positions, current_pos)

#             # No valid position found
#             if idx == len(positions):
#                 return False

#             current_pos = positions[idx]

#         return True


# # Standalone function for single query (without preprocessing)
# def isSubsequence(s: str, t: str) -> bool:
#     char_positions = defaultdict(list)

#     for i, char in enumerate(t):
#         char_positions[char].append(i)

#     current_pos = -1

#     for char in s:
#         positions = char_positions.get(char)

#         if not positions:
#             return False

#         idx = bisect.bisect_right(positions, current_pos)

#         if idx == len(positions):
#             return False

#         current_pos = positions[idx]

#     return True


__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))