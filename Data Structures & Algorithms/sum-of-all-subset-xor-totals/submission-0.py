class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def helper(index, current_xor):
            if index == len(nums):
                return current_xor
            else:
                include = helper(index+1, current_xor ^ nums[index])
                exclude = helper(index+1, current_xor)
            return include + exclude
        return helper(0, 0)