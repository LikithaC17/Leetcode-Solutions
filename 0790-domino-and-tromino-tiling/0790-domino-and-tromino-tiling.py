class Solution(object):
    def numTilings(self, n):
        MOD = 10**9 + 7

        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5

        a, b, c = 1, 2, 5  # dp[1], dp[2], dp[3]

        for i in range(4, n + 1):
            d = (2 * c + a) % MOD
            a, b, c = b, c, d

        return c