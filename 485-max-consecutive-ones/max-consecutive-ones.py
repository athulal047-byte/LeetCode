class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        lar =0
        l =0
        for r in range(len(nums)):
            if nums[r]==0:
                l= r+1
            else:
                w =(r-l)+1
                lar = max(lar,w)
        return lar
        