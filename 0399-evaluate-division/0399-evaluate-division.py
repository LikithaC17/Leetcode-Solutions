class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = {}

        for (a, b), v in zip(equations, values):
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []

            graph[a].append((b, v))
            graph[b].append((a, 1.0 / v))

        def dfs(src, dst, visited):
            if src == dst:
                return 1.0

            visited.add(src)

            for nei, val in graph[src]:
                if nei not in visited:
                    ans = dfs(nei, dst, visited)
                    if ans != -1.0:
                        return val * ans

            return -1.0

        res = []

        for a, b in queries:
            if a not in graph or b not in graph:
                res.append(-1.0)
            else:
                res.append(dfs(a, b, set()))

        return res