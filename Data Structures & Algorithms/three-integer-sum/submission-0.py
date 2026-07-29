class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i, a in enumerate(nums):
            #if the number is > 0 (we alr sorted) we can't get 0 anymore
            if a > 0:
                break
            #if the index is > 0 and a is the same as the last number we 
            #can't use it
            if i > 0 and a == nums[i - 1]:
                continue
            #left is the next from our main and right is the last index
            left = i + 1
            right = len(nums) - 1
            #while the left and right has not collided
            while left < right:
                #if current sum equals 0 add it to our collection
                if a + nums[left] + nums[right] == 0:
                    output.append([a, nums[left], nums[right]])
                    #we still need to iterate
                    left += 1
                    right -= 1
                    #while the left is the same as the last left and 
                #the left is still < the right iterate the left
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                #if its greater we need a smaller number in the sum
                elif a + nums[left] + nums[right] > 0:
                    right -= 1
                #if its less we need a bigger number in the sum
                elif a + nums[left] + nums[right] < 0:
                    left += 1
        #return our collection
        return output