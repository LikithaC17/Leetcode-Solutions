class Solution(object):
    def largestInteger(self, nums, k):
        count = {}

        for i in range(len(nums) - k + 1):
            seen = set()

            for j in range(i, i + k):
                seen.add(nums[j])

            for num in seen:
                count[num] = count.get(num, 0) + 1

        ans = -1

        for num in count:
            if count[num] == 1:
                ans = max(ans, num)

        return ans