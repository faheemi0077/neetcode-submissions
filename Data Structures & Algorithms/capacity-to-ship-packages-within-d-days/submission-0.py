class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_possible_capacity(capacity: int) -> bool:
            for weight in weights:
                if capacity < weight:
                    return False
            track = 1
            cur = 0
            for weight in weights:
                if cur + weight > capacity:
                    track += 1
                    cur = weight
                else:
                    cur += weight
            return track <= days
        lowest = sum(weights)
        low = 1
        high = sum(weights)
        while low <= high:
            mid = low + ((high - low) // 2)
            if is_possible_capacity(mid):
                lowest = mid
                high = mid - 1
            else:
                low = mid + 1
        return lowest