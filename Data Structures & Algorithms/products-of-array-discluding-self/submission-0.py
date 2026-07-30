class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        befores = list()
        afters = list()
        totals = list()
        before = 1
        after = 1
        for i in range(len(nums)):
            befores.append(before)
            before *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            afters = [after] + afters 
            after *= nums[i]
        for i in range(len(nums)):
            prod = befores[i] * afters[i]
            totals.append(prod)
        return totals