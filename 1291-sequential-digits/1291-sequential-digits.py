class Solution(object):
    def sequentialDigits(self, low, high):
        s="123456789"
        ans=[]
        for l in range(2,10):
            for i in range(10-l):
                num=int(s[i:i+l])
                if low<=num<=high:
                    ans.append(num)
        return ans