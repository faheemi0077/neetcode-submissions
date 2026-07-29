class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        right = 0
        left = 0
        mysum = 0
        minsize = float('inf')
        while right < len(nums):
            mysum += nums[right]
            while mysum >= target:
                minsize = min(minsize, (right - left) + 1)
                mysum -= nums[left]
                left += 1
            right += 1
        if minsize == float('inf'):
            return 0
        else:
            return minsize
