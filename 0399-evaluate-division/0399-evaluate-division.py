from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1 / v))

        def dfs(curr, target, visited):
            if curr == target:
                return 1.0

            visited.add(curr)

            for nei, w in graph[curr]:
                if nei not in visited:
                    ans = dfs(nei, target, visited)
                    if ans != -1:
                        return w * ans

            return -1

        res = []

        for a, b in queries:
            if a not in graph or b not in graph:
                res.append(-1.0)
            else:
                res.append(dfs(a, b, set()))

        return res