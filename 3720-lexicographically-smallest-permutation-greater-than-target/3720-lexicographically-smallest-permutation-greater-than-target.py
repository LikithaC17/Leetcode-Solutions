from collections import Counter

class Solution(object):
    def lexGreaterPermutation(self, s, target):
        cnt = Counter(s)
        chars = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        n = len(s)

        def smallest_remaining():
            res = []
            for ch in chars:
                res.extend([ch] * cnt[ch])
            return "".join(res)

        def dfs(i):
            if i == n:
                return None  
            c = target[i]

            
            if cnt[c] > 0:
                cnt[c] -= 1
                suffix = dfs(i + 1)
                cnt[c] += 1
                if suffix is not None:
                    return c + suffix

            
            for ch in chars:
                if ch > c and cnt[ch] > 0:
                    cnt[ch] -= 1
                    ans = ch + smallest_remaining()
                    cnt[ch] += 1
                    return ans

            return None

        ans = dfs(0)
        return "" if ans is None else ans