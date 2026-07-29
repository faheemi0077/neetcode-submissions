class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if i > 0:
                if nums[i] != nums[i-1]:
                    nums[k] = nums[i]
                    k += 1
                else:
                    continue
            else:
                nums[k] = nums[i]
                k += 1
        return k