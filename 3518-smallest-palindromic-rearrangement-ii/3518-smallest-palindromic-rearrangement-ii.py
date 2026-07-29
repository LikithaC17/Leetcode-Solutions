class Solution(object):
    def smallestPalindrome(self, s, k):
        from collections import Counter

        cnt = Counter(s)
        half = sum(cnt.values()) // 2

        fact = [1] * (half + 1)
        for i in range(1, half + 1):
            fact[i] = fact[i - 1] * i

        def count_ways(freq, length):
            result = 1
            remaining = length

            for v in freq:
                if v > 0:
                    result *= fact[remaining] // (fact[remaining - v] * fact[v])
                    if result >= k:
                        return k
                    remaining -= v

            return result

        freq = [cnt[chr(ord('a') + i)] // 2 for i in range(26)]

        if count_ways(freq, half) < k:
            return ""

        left = []
        remaining = half

        while remaining > 0:
            for i in range(26):
                if freq[i] == 0:
                    continue

                freq[i] -= 1
                remaining -= 1

                ways = count_ways(freq, remaining)

                if k > ways:
                    k -= ways
                    freq[i] += 1
                    remaining += 1
                else:
                    left.append(chr(ord('a') + i))
                    break

        left = ''.join(left)

        middle = ""
        for ch in cnt:
            if cnt[ch] % 2:
                middle = ch
                break

        return left + middle + left[::-1]