class Solution(object):
    def uniqueXorTriplets(self, nums):
        size = 1
        while size <= max(nums):
            size <<= 1

        f = [0] * size

        for x in nums:
            f[x] = 1

        def fwht(a, inverse=False):
            n = len(a)
            length = 1

            while length < n:
                for i in range(0, n, length * 2):
                    for j in range(i, i + length):
                        x = a[j]
                        y = a[j + length]
                        a[j] = x + y
                        a[j + length] = x - y
                length *= 2

            if inverse:
                for i in range(n):
                    a[i] //= n

        fwht(f)

        for i in range(size):
            f[i] = f[i] * f[i] * f[i]

        fwht(f, True)

        return sum(1 for x in f if x > 0)