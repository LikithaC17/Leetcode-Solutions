class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        arr = sorted((num, i) for i, num in enumerate(nums))
        ans = nums[:]
        i = 0

        while i < n:
            j = i
            indices = []
            values = []

            while j < n and (j == i or arr[j][0] - arr[j - 1][0] <= limit):
                values.append(arr[j][0])
                indices.append(arr[j][1])
                j += 1

            indices.sort()
            for idx, val in zip(indices, values):
                ans[idx] = val

            i = j

        return ans