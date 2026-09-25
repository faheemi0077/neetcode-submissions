class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            left = i+1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    triplet = [nums[i], nums[left], nums[right]]
                    if triplet not in triplets:
                        triplets.append(triplet)
                    left += 1
                    right -= 1
        return triplets