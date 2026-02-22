'''
Problem URL: https://leetcode.com/problems/range-sum-query-mutable/description/

Given an integer array nums, handle multiple queries of the following types:
Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example 1:
Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8

Constraints:
1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 104 calls will be made to update and sumRange.
'''

# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.n = len(nums)
#         self.tree = [0] * 2 * self.n
#         for i in range(self.n):
#             self.tree[i + self.n] = nums[i]
#         for i in range(self.n-1, 0, -1):
#             self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
#         print(self.tree)

#     def update(self, index: int, val: int) -> None:
#         index += self.n
#         self.tree[index] = val
#         while index > 1:
#             self.tree[index//2] = self.tree[index] + self.tree[index^1]
#             index //= 2

#     def sumRange(self, left: int, right: int) -> int:
#         left += self.n
#         right += self.n
#         res = 0
#         while left <= right:
#             if left & 1:
#                 # if left odd:
#                 res += self.tree[left]
#                 left += 1
#             if right & 1 ==0:
#                 # if right even
#                 res += self.tree[right]
#                 right -= 1
#             left //= 2
#             right //= 2
#         return res 





# class TreeNode:
#     def __init__(self, val, start, end, left_child = None, right_child = None):
#         self.val = val     # sum of the interval belongs to this node
#         self.start = start # start of the node's interval
#         self.end = end     # end of the node's interval
#         self.left_child = left_child   # left child node
#         self.right_child = right_child # right child node

# class SegmentTree:
#     def __init__(self, nums):
#         self.nums = nums
#         self.root = self.build(0, len(nums) - 1)
    
#     def build(self, start, end):
#         if start == end:
#             return TreeNode(self.nums[start], start, end)
#         left_child = self.build(start, (start+end)//2)
#         right_child = self.build((start+end)//2 + 1, end)
#         return TreeNode(left_child.val + right_child.val, start, end, left_child, right_child)
    
#     def update(self, root, index, value):
#         if root.start == root.end and index == root.start: # target
#             root.val = value
#             return value
#         if root.start > index or root.end < index:
#             return root.val
#         root.val = self.update(root.left_child, index, value) + self.update(root.right_child, index, value)
#         return root.val

#     def query(self, root, left, right):
#         if root.start > right or root.end < left: return 0
#         if root.start >= left and root.end <= right: return root.val
#         return self.query(root.left_child, left, right) + self.query(root.right_child, left, right)

# class NumArray:
#     def __init__(self, nums: List[int]):
#         self.tree = SegmentTree(nums)
#         self.root = self.tree.root

#     def update(self, index: int, val: int) -> None:
#         self.tree.update(self.root, index, val)

#     def sumRange(self, left: int, right: int) -> int:
#         return self.tree.query(self.root, left, right)





# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.nums = nums
#         self.sum = sum(nums)
#         self.d = {}

#     def update(self, index: int, val: int) -> None:
#         self.sum += val-self.nums[index]
#         self.nums[index] = val
#         self.d = {} 
        

#     def sumRange(self, left: int, right: int) -> int:
#         if (left,right) in self.d:
#             return self.d[(left,right)]
#         elif (right-left)>=(len(self.nums))//2:
#             res = self.sum-sum(self.nums[:left])-sum(self.nums[right+1:])
#         else:
#             res = sum(self.nums[left:right+1])
#         self.d[(left,right)] = res
#         return res






# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.nums = nums
#         self.n = len(nums)
#         self.tree = [0]*(self.n +1)
#         for i in range(1, self.n + 1):
#             self.tree[i] += self.nums[i-1]
#             j = i + (i & -i)
#             if j <= self.n:
#                 self.tree[j] += self.tree[i]

#     def update(self, index: int, val: int) -> None:
#         delta = val - self.nums[index] 
#         self.nums[index] = val
#         i = index + 1
#         while i <= self.n:
#             self.tree[i] +=delta
#             i += i & -i
#     def sumRange(self, left: int, right: int) -> int:
#         def get_sum(i):
#             s = 0
#             idx = i + 1
#             while idx > 0:
#                 s += self.tree[idx]
#                 idx -= idx & -idx
#             return s
#         if left == 0:
#             return get_sum(right)
#         return get_sum(right) - get_sum(left-1)







class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = [0] * self.n
        self.bit = [0] * (self.n + 1)

        for i, num in enumerate(nums):
            self.update(i, num)



    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val

        index += 1
        while index <= self.n:
            self.bit[index] += delta

            lsb = -index & index
            index += lsb

    def _query(self, index: int) -> int:
        res = 0

        index += 1
        while index > 0:
            res += self.bit[index]

            lsb = -index & index
            index -= lsb
        return res

    def sumRange(self, left: int, right: int) -> int:
        return self._query(right) - self._query(left - 1)

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)