class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            x = nums[i]
            s = 0
            while x:
                s += x % 10
                x //= 10
            if s == i:
                return i
        return -1