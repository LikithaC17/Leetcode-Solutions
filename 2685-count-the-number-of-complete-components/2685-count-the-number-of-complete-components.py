class Solution(object):
    def countCompleteComponents(self, n, edges):
        g=[[] for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        vis=[False]*n
        ans=0
        for i in range(n):
            if not vis[i]:
                comp=[]
                stack=[i]
                vis[i]=True
                while stack:
                    u=stack.pop()
                    comp.append(u)
                    for v in g[u]:
                        if not vis[v]:
                            vis[v]=True
                            stack.append(v)
                k=len(comp)
                e=0
                for u in comp:
                    e+=len(g[u])
                if e==k*(k-1):
                    ans+=1
        return ans