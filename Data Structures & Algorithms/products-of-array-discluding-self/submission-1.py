class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        befores = list()
        afters = list()
        ans = list()
        for i in range(len(nums)):
            if i == 0:
                befores.append(1)
            else:
                befores.append(befores[i - 1] * nums[i - 1])
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                afters.append(1)
            else:
                afters.append(afters[len(nums) - 1 - i - 1] * nums[i + 1])
        j = 0
        k = len(afters) - 1
        while j <= len(nums) - 1:
            ans.append(befores[j] * afters[k])
            j += 1
            k -= 1
        return ans