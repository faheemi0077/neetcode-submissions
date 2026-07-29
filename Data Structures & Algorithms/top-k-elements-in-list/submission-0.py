from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topk = []
        occourences = defaultdict(int)
        for num in nums:
            occourences[num] += 1
        return sorted(occourences, key=occourences.get, reverse=True)[:k]

        