class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(r, c, size):
            first = grid[r][c]
            same = True

            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != first:
                        same = False
                        break
                if not same:
                    break

            if same:
                return Node(bool(first), True)

            half = size // 2
            return Node(
                True,
                False,
                build(r, c, half),
                build(r, c + half, half),
                build(r + half, c, half),
                build(r + half, c + half, half)
            )

        return build(0, 0, len(grid))