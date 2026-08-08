class Solution(object):
    def validSequence(self, word1, word2):
        n = len(word1)
        m = len(word2)

        suf = [0] * (n + 1)
        j = m - 1

        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1]
            if j >= 0 and word1[i] == word2[j]:
                suf[i] += 1
                j -= 1

        ans = []
        pos = 0
        j = 0
        changed = False

        while pos < n and j < m:
            if word1[pos] == word2[j]:
                ans.append(pos)
                pos += 1
                j += 1
            elif not changed:
                if suf[pos + 1] >= m - j - 1:
                    ans.append(pos)
                    pos += 1
                    j += 1
                    changed = True
                else:
                    pos += 1
            else:
                pos += 1

        if j == m and len(ans) == m:
            return ans

        return []