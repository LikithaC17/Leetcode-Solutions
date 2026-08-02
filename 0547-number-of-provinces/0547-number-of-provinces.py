class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n

        def dfs(city):
            visited[city] = True
            for nei in range(n):
                if isConnected[city][nei] == 1 and not visited[nei]:
                    dfs(nei)

        provinces = 0

        for i in range(n):
            if not visited[i]:
                dfs(i)
                provinces += 1

        return provinces