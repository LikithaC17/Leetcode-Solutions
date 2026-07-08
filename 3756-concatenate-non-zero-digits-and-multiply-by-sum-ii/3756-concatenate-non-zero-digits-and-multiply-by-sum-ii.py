class Solution(object):
    def sumAndMultiply(self,s,queries):
        MOD=10**9+7
        m=len(s)

        
        digits=[]
        pos=[]

        for i,ch in enumerate(s):
            if ch!='0':
                digits.append(int(ch))
                pos.append(i)

        k=len(digits)

        
        if k==0:
            return[0]*len(queries)

       
        prefix_sum=[0]*(k+1)
        for i in range(k):
            prefix_sum[i+1]=prefix_sum[i]+digits[i]

        
        pow10=[1]*(k+1)
        for i in range(1,k+1):
            pow10[i]=(pow10[i-1]*10)%MOD

        
        P=[0]*(k+1)
        for i in range(k):
            P[i+1]=(P[i]*10+digits[i])%MOD

        import bisect

        ans=[]

        for l,r in queries:
            left=bisect.bisect_left(pos,l)
            right=bisect.bisect_right(pos,r)-1

            if left>right:
                ans.append(0)
                continue

            length=right-left+1

            
            x=(P[right+1]-P[left]*pow10[length])%MOD

            
            digit_sum=prefix_sum[right+1]-prefix_sum[left]

            ans.append((x*digit_sum)%MOD)

        return ans