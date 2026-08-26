from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        need = Counter(t)
        window = {}
        have = 0
        required = len(need)

        left = 0
        min_len = float("inf")
        res = [-1, -1]

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = [left, right]

                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return "" if min_len == float("inf") else s[l:r+1]