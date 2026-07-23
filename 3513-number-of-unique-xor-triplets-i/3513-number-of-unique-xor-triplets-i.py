class Solution(object):
    def uniqueXorTriplets(self, nums):
        n = len(nums)
        
        if n < 3:
            return n
        
        ans = 1
        while ans <= n:
            ans *= 2
        
        return ans