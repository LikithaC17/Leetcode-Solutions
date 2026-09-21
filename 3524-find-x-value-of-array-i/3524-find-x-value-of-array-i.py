class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        dp=[0]*k
        ans=[0]*k
        for num in nums:
            cur=[0]*k
            m=num%k
            cur[m]+=1
            for r,c in enumerate(dp):
                if c:
                    cur[(r*m)%k]+=c
            dp=cur
            for r,c in enumerate(dp):
                ans[r]+=c
        return ans