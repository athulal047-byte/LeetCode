class Solution(object):
    def maxSubArray(self, nums):
        maxsub=nums[0]
        currsum=0

        for i in nums:
            if currsum<0:
                currsum =0
            currsum = currsum + i
            maxsub=max(currsum,maxsub) 
        return maxsub