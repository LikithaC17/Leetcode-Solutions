class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        total = 0
        last = {}

        for c in s:
            new = (total + 1) % MOD
            total = (total + new - last.get(c, 0)) % MOD
            last[c] = new

        return total