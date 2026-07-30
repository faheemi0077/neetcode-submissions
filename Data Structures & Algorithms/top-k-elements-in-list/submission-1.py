class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = dict()
        most = list()
        for i in range(len(nums)):
            if nums[i] not in frequencies.keys():
                frequencies[nums[i]] = 1
            else:
                frequencies[nums[i]] += 1
        sorted_frequencies = dict(sorted(frequencies.items(), key=lambda item: item[1], reverse=True))
        j = 0
        for key in sorted_frequencies.keys():
            most.append(key)
            j += 1
            if j == k:
                return most