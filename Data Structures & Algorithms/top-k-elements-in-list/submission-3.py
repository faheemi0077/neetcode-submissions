import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = dict()
        for num in nums:
            if num not in frequencies.keys():
                frequencies[num] = 1
            else:
                frequencies[num] += 1
        ordered = list()
        topk = heapq.nlargest(k, frequencies, key=frequencies.get)
        return topk