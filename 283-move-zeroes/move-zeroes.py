class Solution(object):
    def moveZeroes(self, nums):
        l=0
        for r in range(len(nums)):
            if nums[r] == 0:
                continue
            else:
                nums[l],nums[r]=nums[r],nums[l]
                l=l+1
        
        