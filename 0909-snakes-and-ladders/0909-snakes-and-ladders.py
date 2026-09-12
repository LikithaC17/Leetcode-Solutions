from collections import deque

class Solution:
    def snakesAndLadders(self, board):
        n = len(board)

        def position(square):
            r = (square - 1) // n
            c = (square - 1) % n
            if r % 2 == 1:
                c = n - 1 - c
            return n - 1 - r, c

        queue = deque([(1, 0)])
        visited = {1}

        while queue:
            square, moves = queue.popleft()

            if square == n * n:
                return moves

            for nxt in range(square + 1, min(square + 6, n * n) + 1):
                row, col = position(nxt)
                dest = board[row][col] if board[row][col] != -1 else nxt

                if dest not in visited:
                    visited.add(dest)
                    queue.append((dest, moves + 1))

        return -1