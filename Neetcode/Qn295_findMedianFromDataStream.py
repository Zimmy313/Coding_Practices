import heapq

class MedianFinder:

    def __init__(self):
        self.minheap = []  # larger half, min-heap
        self.maxheap = []  # smaller half, simulated max-heap using negatives

        # Invariant:
        # len(maxheap) == len(minheap)
        # or
        # len(maxheap) == len(minheap) + 1

    def addNum(self, num: int) -> None:

        # Put num into the appropriate half
        if not self.maxheap or num <= -self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)

            # maxheap can have at most one extra element
            if len(self.maxheap) > len(self.minheap) + 1:
                temp = heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, -temp)

        else:
            heapq.heappush(self.minheap, num)

            # minheap should never be larger
            if len(self.minheap) > len(self.maxheap):
                temp = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -temp)

    def findMedian(self) -> float:

        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] - self.maxheap[0]) / 2

        return -self.maxheap[0]