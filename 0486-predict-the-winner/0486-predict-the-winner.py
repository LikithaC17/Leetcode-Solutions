class Solution(object):
    def predictTheWinner(self, nums):
        memo = {}

        def dfs(l, r):
            if l == r:
                return nums[l]

            if (l, r) in memo:
                return memo[(l, r)]

            take_left = nums[l] - dfs(l + 1, r)
            take_right = nums[r] - dfs(l, r - 1)

            memo[(l, r)] = max(take_left, take_right)
            return memo[(l, r)]

        return dfs(0, len(nums) - 1) >= 0