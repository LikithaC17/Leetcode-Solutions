from collections import Counter

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        cnt = Counter(digits)
        ans = 0

        for num in range(100, 1000, 2):
            need = Counter(map(int, str(num)))
            if all(cnt[d] >= need[d] for d in need):
                ans += 1

        return ans