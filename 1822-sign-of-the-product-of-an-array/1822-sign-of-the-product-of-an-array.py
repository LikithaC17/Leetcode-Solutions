class Solution(object):
    def arraySign(self, nums):
        negative = 0

        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                negative += 1

        if negative % 2 == 0:
            return 1
        return -1