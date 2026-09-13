from collections import Counter

class Solution:
    def largestOverlap(self, img1, img2):
        ones1 = []
        ones2 = []

        n = len(img1)

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    ones1.append((i, j))
                if img2[i][j] == 1:
                    ones2.append((i, j))

        counter = Counter()

        for x1, y1 in ones1:
            for x2, y2 in ones2:
                counter[(x2 - x1, y2 - y1)] += 1

        return max(counter.values(), default=0)