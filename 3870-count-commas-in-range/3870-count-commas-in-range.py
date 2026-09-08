class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        threshold = 1000
        commas = 1

        while threshold <= n:
            ans += (n - threshold + 1) * commas
            threshold *= 1000
            commas += 1

        return ans