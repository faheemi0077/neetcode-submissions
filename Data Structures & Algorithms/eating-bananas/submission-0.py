import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid_rate(k: int) -> bool:
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / k)
            return hours <= h
        lowest = max(piles)
        low = 1
        high = max(piles)
        while low <= high:
            mid = low + ((high - low) // 2)
            if valid_rate(mid):
                lowest = mid
                high = mid - 1
            else:
                low = mid + 1
        return lowest