class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = dict()
        for i in range(len(nums)):
            ext = target - nums[i]
            if ext in complements.keys():
                return [min(i, complements[ext]), max(i, complements[ext])]
            else:
                complements[nums[i]] = i