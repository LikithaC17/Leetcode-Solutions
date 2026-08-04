# The guess API is already defined for you.
# def guess(num):
#     if num == pick: return 0
#     elif num > pick: return -1
#     else: return 1

class Solution(object):
    def guessNumber(self, n):
        left, right = 1, n

        while left <= right:
            mid = left + (right - left) // 2
            res = guess(mid)

            if res == 0:
                return mid
            elif res == -1:
                right = mid - 1
            else:
                left = mid + 1