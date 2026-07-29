class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] in window:
                return True
            else:
                window.add(nums[right])
                right += 1
            if len(window) > k:
                window.remove(nums[left])
                left += 1
        return False