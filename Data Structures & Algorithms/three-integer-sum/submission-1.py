class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                complement = 0 - nums[i]
                if nums[j] + nums[k] == complement:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] > complement:
                    k -= 1
                elif nums[j] + nums[k] < complement:
                    j += 1
        uniques = []
        for i in range(len(triplets)):
            if triplets[i] not in uniques:
                uniques.append(triplets[i])
        return uniques