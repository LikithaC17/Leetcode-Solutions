from bisect import bisect_left

class Solution(object):
    def gcdValues(self, nums, queries):
        mx=max(nums)
        freq=[0]*(mx+1)
        for x in nums:
            freq[x]+=1

        cnt=[0]*(mx+1)
        for i in range(1,mx+1):
            for j in range(i,mx+1,i):
                cnt[i]+=freq[j]

        pairs=[0]*(mx+1)
        for i in range(mx,0,-1):
            c=cnt[i]
            pairs[i]=c*(c-1)//2
            j=i*2
            while j<=mx:
                pairs[i]-=pairs[j]
                j+=i

        vals=[]
        pref=[]
        s=0
        for i in range(1,mx+1):
            if pairs[i]:
                s+=pairs[i]
                vals.append(i)
                pref.append(s)

        ans=[]
        for q in queries:
            ans.append(vals[bisect_left(pref,q+1)])
        return ans