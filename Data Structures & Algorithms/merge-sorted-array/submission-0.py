class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        last1 = len(nums1) - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[last1] = nums1[p1]
                p1 -= 1
                last1 -= 1
            elif nums1[p1] < nums2[p2]:
                nums1[last1] = nums2[p2]
                p2 -= 1
                last1 -= 1
        while p2 >= 0:
            nums1[last1] = nums2[p2]
            p2 -= 1
            last1 -= 1
