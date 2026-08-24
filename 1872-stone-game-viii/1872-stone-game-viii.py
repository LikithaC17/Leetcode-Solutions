class Solution(object):
    def stoneGameVIII(self, stones):
        n = len(stones)

        # Prefix sums
        prefix = stones[:]
        for i in range(1, n):
            prefix[i] += prefix[i - 1]

        dp = prefix[-1]

        for i in range(n - 2, 0, -1):
            dp = max(dp, prefix[i] - dp)

        return dp