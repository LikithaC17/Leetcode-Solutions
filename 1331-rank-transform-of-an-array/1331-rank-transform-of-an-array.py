class Solution(object):
    def arrayRankTransform(self, arr):
        rank={}
        s=sorted(set(arr))
        for i,v in enumerate(s):
            rank[v]=i+1
        return [rank[x] for x in arr]