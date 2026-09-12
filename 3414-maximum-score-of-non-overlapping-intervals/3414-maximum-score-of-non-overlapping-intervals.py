from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))

        arr.sort()
        starts = [x[0] for x in arr]

        nxt = [0] * n
        for i in range(n):
            nxt[i] = bisect_right(starts, arr[i][1])

        score = [[0] * (n + 1) for _ in range(5)]
        path = [[() for _ in range(n + 1)] for _ in range(5)]

        for i in range(n - 1, -1, -1):
            _, _, w, idx = arr[i]

            for k in range(1, 5):
                skip_score = score[k][i + 1]
                skip_path = path[k][i + 1]

                take_score = w + score[k - 1][nxt[i]]
                take_path = tuple(sorted((idx,) + path[k - 1][nxt[i]]))

                if take_score > skip_score or (
                    take_score == skip_score and take_path < skip_path
                ):
                    score[k][i] = take_score
                    path[k][i] = take_path
                else:
                    score[k][i] = skip_score
                    path[k][i] = skip_path

        return list(path[4][0])