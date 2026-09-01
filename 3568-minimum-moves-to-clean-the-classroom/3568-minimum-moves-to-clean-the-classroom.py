from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter = {}
        start = None
        idx = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == "S":
                    start = (i, j)
                elif classroom[i][j] == "L":
                    litter[(i, j)] = idx
                    idx += 1

        target = (1 << idx) - 1
        q = deque([(start[0], start[1], energy, 0, 0)])
        best = {(start[0], start[1], 0): energy}
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            r, c, e, mask, steps = q.popleft()

            if mask == target:
                return steps

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if classroom[nr][nc] == "X":
                    continue
                if e == 0:
                    continue

                ne = e - 1
                if classroom[nr][nc] == "R":
                    ne = energy

                nmask = mask
                if (nr, nc) in litter:
                    nmask |= 1 << litter[(nr, nc)]

                key = (nr, nc, nmask)
                if ne > best.get(key, -1):
                    best[key] = ne
                    q.append((nr, nc, ne, nmask, steps + 1))

        return -1