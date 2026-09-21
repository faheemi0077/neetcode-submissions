class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][len(matrix[mid]) - 1]:
                left = mid + 1
            else:
                innerleft = 0
                innerright = len(matrix[mid]) - 1
                while innerleft <= innerright:
                    innermid = innerleft + ((innerright - innerleft) // 2)
                    if matrix[mid][innermid] < target:
                        innerleft = innermid + 1
                    elif matrix[mid][innermid] > target:
                        innerright = innermid - 1
                    else:
                        return True
                return False
        return False