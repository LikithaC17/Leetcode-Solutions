import heapq

class Solution(object):
    def totalCost(self, costs, k, candidates):
        n = len(costs)

        left_heap = []
        right_heap = []

        left = 0
        right = n - 1

        # Fill left heap
        while left < candidates and left <= right:
            heapq.heappush(left_heap, costs[left])
            left += 1

        # Fill right heap
        while right >= n - candidates and right >= left:
            heapq.heappush(right_heap, costs[right])
            right -= 1

        ans = 0

        for _ in range(k):
            if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
                ans += heapq.heappop(left_heap)
                if left <= right:
                    heapq.heappush(left_heap, costs[left])
                    left += 1
            else:
                ans += heapq.heappop(right_heap)
                if left <= right:
                    heapq.heappush(right_heap, costs[right])
                    right -= 1

        return ans