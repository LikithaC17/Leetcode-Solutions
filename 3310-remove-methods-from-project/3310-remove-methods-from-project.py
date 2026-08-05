from collections import defaultdict, deque
class Solution(object):
    def remainingMethods(self, n, k, invocations):
        graph = defaultdict(list)

        for u, v in invocations:
            graph[u].append(v)

        
        suspicious = set()
        q = deque([k])
        suspicious.add(k)

        while q:
            node = q.popleft()
            for nei in graph[node]:
                if nei not in suspicious:
                    suspicious.add(nei)
                    q.append(nei)

        
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))

        
        return [i for i in range(n) if i not in suspicious]