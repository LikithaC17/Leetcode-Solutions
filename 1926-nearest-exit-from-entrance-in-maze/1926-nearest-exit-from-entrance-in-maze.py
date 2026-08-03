from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        m, n = len(maze), len(maze[0])
        q = deque()
        
        r, c = entrance
        q.append((r, c, 0))
        maze[r][c] = '+'   

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            x, y, steps = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':
                    if nx == 0 or nx == m - 1 or ny == 0 or ny == n - 1:
                        return steps + 1

                    maze[nx][ny] = '+'
                    q.append((nx, ny, steps + 1))

        return -1