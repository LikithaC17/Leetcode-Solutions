# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def maxLevelSum(self, root):
        q = deque([root])
        level = 1
        ans = 1
        maxSum = float("-inf")

        while q:
            s = 0

            for _ in range(len(q)):
                node = q.popleft()
                s += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if s > maxSum:
                maxSum = s
                ans = level

            level += 1

        return ans