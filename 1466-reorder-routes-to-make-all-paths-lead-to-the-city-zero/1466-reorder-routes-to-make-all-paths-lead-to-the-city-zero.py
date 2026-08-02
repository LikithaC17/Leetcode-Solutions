class Solution(object):
    def minReorder(self, n, connections):
        graph = [[] for _ in range(n)]

        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            changes = 0

            for nei, cost in graph[node]:
                if not visited[nei]:
                    changes += cost + dfs(nei)

            return changes

        return dfs(0)