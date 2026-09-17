class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n=len(arr)
        best=[float('inf')]*n
        left=0
        curr=0
        ans=float('inf')

        for right in range(n):
            curr+=arr[right]
            while curr>target:
                curr-=arr[left]
                left+=1

            if curr==target:
                length=right-left+1
                if left>0:
                    ans=min(ans,length+best[left-1])
                best[right]=min(best[right-1] if right>0 else float('inf'),length)
            else:
                best[right]=best[right-1] if right>0 else float('inf')

        return -1 if ans==float('inf') else ans