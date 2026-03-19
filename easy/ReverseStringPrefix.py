'''
Problem URL: https://leetcode.com/problems/reverse-string-prefix/description/

You are given a string s and an integer k.
Reverse the first k characters of s and return the resulting string.

Example 1:
Input: s = "abcd", k = 2
Output: "bacd"
Explanation:​​​​​​​
The first k = 2 characters "ab" are reversed to "ba". The final resulting string is "bacd".

Example 2:
Input: s = "xyz", k = 3
Output: "zyx"
Explanation:
The first k = 3 characters "xyz" are reversed to "zyx". The final resulting string is "zyx".

Example 3:
Input: s = "hey", k = 1
Output: "hey"
Explanation:
The first k = 1 character "h" remains unchanged on reversal. The final resulting string is "hey".

Constraints:
1 <= s.length <= 100
s consists of lowercase English letters.
1 <= k <= s.length
'''

class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        # n = len(s)
        # slk = list(s[:k])
        # x = 0
        # y = k-1
        # while(x<y):
        #     slk[x], slk[y] = slk[y], slk[x]
        #     x += 1
        #     y -= 1
        # return "".join(slk) + s[k:]





        # return s[:k][::-1]+s[k:]




        # chars = [c for c in s]
        # for i in range(k // 2):
        #     # 1 2 3 4 5 6 7 8 9, k=3
        #     # 3 2 1 4 5 6 7 8 9
        #     chars[i], chars[k-i-1] = chars[k-i-1], chars[i]
        # return ''.join(chars)






        # s=list(s)
        # l=0
        # r=k-1
        # while l<r:
        #     s[l],s[r]=s[r],s[l]
        #     l+=1
        #     r-=1
        # return "".join(s)





        # lst=list(s)
        # l,r=0,k-1
        # while l<r:
        #     lst[l],lst[r]=lst[r],lst[l]
        #     l+=1
        #     r-=1
        # return ''.join(lst)






        li = list(s[0:k])
        if k <= 1: return s
        p1, p2 = 0, k - 1
        while p2 > p1:
            li[p1], li[p2] = li[p2], li[p1]
            p1 += 1
            p2 -= 1
        return "".join(li) + s[k::]