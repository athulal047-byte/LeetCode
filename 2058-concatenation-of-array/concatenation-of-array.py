class Solution(object):
    def getConcatenation(self, nums):
        n = len(nums)
        b=2*n
        ans=[]
        for i in range(n):
            ans.append(nums[i])
        for i in range(n):
            ans.append(nums[i])
        return ans

        