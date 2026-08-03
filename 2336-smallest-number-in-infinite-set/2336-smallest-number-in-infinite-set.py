import heapq

class SmallestInfiniteSet(object):

    def __init__(self):
        self.curr = 1
        self.heap = []
        self.in_heap = set()

    def popSmallest(self):
        if self.heap:
            x = heapq.heappop(self.heap)
            self.in_heap.remove(x)
            return x

        x = self.curr
        self.curr += 1
        return x

    def addBack(self, num):
        if num < self.curr and num not in self.in_heap:
            heapq.heappush(self.heap, num)
            self.in_heap.add(num)