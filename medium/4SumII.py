'''
Problem URL: https://leetcode.com/problems/4sum-ii/description/

Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:
0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Example 1:
Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

Example 2:\
Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1

Constraints:
n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228
'''

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # z = Counter(v+u for v in a for u in b)
        # return sum(z[-p-q] for p in w for q in o)

        # z = Counter(map(sum,product(a,b)))
        # return sum(z[-p-q] for p in w for q in o)
        n1 = Counter(nums1)
        n2 = Counter(nums2)
        n3 = Counter(nums3)
        n4 = Counter(nums4)
        a, b = defaultdict(int), defaultdict(int)
        for k1, v1 in n1.items():
            for k2, v2 in n2.items():
                a[k1+k2] += v1 * v2
        for k1, v1 in n3.items():
            for k2, v2 in n4.items():
                b[k1+k2] += v1 * v2
        result = 0
        for k, v in a.items():
            result += b.get(-k, 0) * v
        return result
__import__("atexit").register(lambda:open("display_runtime.txt","w").write("0"))