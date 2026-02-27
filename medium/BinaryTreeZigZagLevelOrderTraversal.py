'''
Problem URL: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # if not root:
        #     return []
        
        # results = []
        # queue = deque([root])
        # left_to_right = True # Our "Directional Toggle"
        
        # while queue:
        #     level_size = len(queue)
        #     # Use a deque for the current level to allow efficient flipping
        #     current_level = deque()
            
        #     for _ in range(level_size):
        #         node = queue.popleft()
                
        #         # Interleaving Logic: 
        #         # Instead of reversing the list at the end (O(N)),
        #         # we decide where to "inject" the data as it arrives.
        #         if left_to_right:
        #             current_level.append(node.val)
        #         else:
        #             current_level.appendleft(node.val)
                
        #         # Always add children to the main queue in standard order
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
            
        #     results.append(list(current_level))
        #     # Flip the "switch" for the next level/time-slot
        #     left_to_right = not left_to_right
            
        # return results






        q=collections.deque()
        q.append(root)
        counter=0
        op=[]
        while q:
            qlen=len(q)
            temp=[]
            for _ in range(qlen):
                cur=q.popleft()
                if cur:
                    temp.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
            counter+=1
            if temp:
                if counter%2==0:
                    temp.reverse()
                op.append(temp)
        return op