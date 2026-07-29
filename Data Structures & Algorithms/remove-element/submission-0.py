class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        w = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = nums[w]
                w += 1
            elif nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k