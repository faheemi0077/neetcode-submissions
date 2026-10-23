class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = list()
        for i in range(len(nums)):
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplets.append([nums[i], nums[j], nums[k]])
                        k -= 1
                    elif nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
        actuals = list()
        for i in range(len(triplets)):
            if triplets[i] not in actuals:
                actuals.append(triplets[i])
        return actuals