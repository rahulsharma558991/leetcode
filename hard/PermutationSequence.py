'''
Problem URL: https://leetcode.com/problems/permutation-sequence/description

The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Example 1:
Input: n = 3, k = 3
Output: "213"

Example 2:
Input: n = 4, k = 9
Output: "2314"

Example 3:
Input: n = 3, k = 1
Output: "123"

Constraints:
1 <= n <= 9
1 <= k <= n!
'''

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # from math import factorial
        # nums = list(range(1, n + 1))
        # fact = factorial(n) // n
        # k -= 1
        # res = []
        # while nums:
        #     res.append(str(nums[k // fact]))
        #     nums.pop(k // fact)
        #     if not nums:
        #         break
        #     k %= fact
        #     fact //= len(nums)
        # return "".join(res)




        # # n = Zahlen, die in n! enthalten sind -> n = 3 bedeutet 3! = 3*2*1 -> Ziffern 1,2,3
        # # k = Anzahl an Kombination
        # # str = ergebnis in res gespeichert
        # res = ''
        # numbers = [str(i) for i in range(1, n+1)]
        # k -= 1
        # while numbers:
        #     fact = math.factorial(len(numbers)-1)
        #     i = k // fact
        #     res += numbers[i]
        #     numbers.pop(i)
        #     k = k % fact
        # return res






        # return "".join(str(x) for x in next(islice(permutations(range(1,n+1)), k-1 ,None)))







        # nums = range(1, n + 1)
        # p = permutations(nums)
        # for i in range(k - 1):
        #     next(p)  
        # target = next(p)
        # return "".join(map(str, target))






        # s='123456789'[:n]
        # i=0
        # for x in itertools.permutations(s):
        #     i+=1
        #     if i==k:
        #         return ''.join(x)
        # return -1






        nums = [str(i) for i in range(1, n + 1)]
        count = 0
        result = ""
        def backtrack(path, options):
            nonlocal count, result
            if result:
                return
            if not options:
                count += 1
                if count == k:
                    result = "".join(path)
                return
            for i in range(len(options)):
                path.append(options[i])
                backtrack(path, options[:i] + options[i+1:])
                path.pop()
        backtrack([], nums)
        return result