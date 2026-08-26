class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        n = len(s)
        best = ""

        for i in range(n):
            ones = 0
            for j in range(i, n):
                if s[j] == '1':
                    ones += 1

                if ones == k:
                    sub = s[i:j+1]
                    if (best == "" or
                        len(sub) < len(best) or
                        (len(sub) == len(best) and sub < best)):
                        best = sub
                    break

                if ones > k:
                    break

        return best