class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        size = 1

        while size < n:
            size *= 2

        tree = [(None, None, 0, 0, 0, 0)] * (2 * size)

        for i in range(n):
            c = s[i]
            tree[size + i] = (c, c, 1, 1, 1, 1)

        def merge(a, b):
            if a[2] == 0:
                return b
            if b[2] == 0:
                return a

            left = a[0]
            right = b[1]
            length = a[2] + b[2]
            prefix = a[3]
            suffix = b[4]
            best = max(a[5], b[5])

            if a[1] == b[0]:
                best = max(best, a[4] + b[3])

                if a[3] == a[2]:
                    prefix = a[2] + b[3]

                if b[4] == b[2]:
                    suffix = a[4] + b[2]

            return (left, right, length, prefix, suffix, best)

        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[i * 2], tree[i * 2 + 1])

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            p = size + idx
            tree[p] = (ch, ch, 1, 1, 1, 1)

            p //= 2

            while p:
                tree[p] = merge(tree[p * 2], tree[p * 2 + 1])
                p //= 2

            ans.append(tree[1][5])

        return ans