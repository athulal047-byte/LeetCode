class Solution(object):
    def getConcatenation(self, nums):
        n = len(nums)
        ans=[]
        for i in range(2):
            for j in range (n):
                ans.append(nums[j])
        return ans

        