'''
Problem URL: https://leetcode.com/problems/maximum-number-of-balloons/description/

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0

Constraints:
1 <= text.length <= 104
text consists of lower case English letters only.

Note: This question is the same as 2287: Rearrange Characters to Make Target String.
'''

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Approach: Frequency Count with Maps
        # Create a frequency map for the input string
        # freqMap = {}
        # for c in text:
        #     freqMap[c] = freqMap.get(c, 0) + 1

        # # Store the required frequencies of each character in 'balloon'
        # balloon = "balloon"

        # # Calculate the max number of "balloon" words
        # maxBalloons = float('inf')
        # balloonFreq = {}
        # for c in balloon:
        #     balloonFreq[c] = balloonFreq.get(c, 0) + 1

        # # Calculate the max possible number of "balloon" we can form
        # for key, count in balloonFreq.items():
        #     maxBalloons = min(maxBalloons, freqMap.get(key, 0) // count)

        # return 0 if maxBalloons == float('inf') else maxBalloons



        # Approach: Frequency Count with Arrays
        # Frequency array for all lowercase characters
        # count = [0] * 26
        # for c in text:
        #     if 'a' <= c <= 'z':
        #         count[ord(c) - ord('a')] += 1

        # # Calculate the minimum number of "balloon" we can form
        # minBalloons = float('inf')

        # # Check against required characters
        # minBalloons = min(minBalloons, count[ord('b') - ord('a')])
        # minBalloons = min(minBalloons, count[ord('a') - ord('a')])
        # minBalloons = min(minBalloons, count[ord('l') - ord('a')] // 2)
        # minBalloons = min(minBalloons, count[ord('o') - ord('a')] // 2)
        # minBalloons = min(minBalloons, count[ord('n') - ord('a')])

        # return 0 if minBalloons == float('inf') else minBalloons




        # Approach: Python single liner
        cnt = Counter(text)
        return min(cnt['b'], cnt['a'], cnt['n'], cnt['l'] // 2, cnt['o'] // 2)