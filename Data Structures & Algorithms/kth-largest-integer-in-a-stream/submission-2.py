import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.klargest = heapq.nlargest(self.k, nums)
        heapq.heapify(self.klargest)

    def add(self, val: int) -> int:
        if len(self.klargest) < self.k:
            heapq.heappush(self.klargest, val)
        else:
            if val > self.klargest[0]:
                heapq.heapreplace(self.klargest, val)
        return self.klargest[0]