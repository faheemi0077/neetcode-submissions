import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        klargest = []
        for i in range(len(nums)):
            if len(klargest) < k:
                heapq.heappush(klargest, nums[i])
            else:
                if nums[i] > klargest[0]:
                    heapq.heapreplace(klargest, nums[i])
        return klargest[0]