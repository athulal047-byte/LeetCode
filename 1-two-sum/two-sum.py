class Solution(object):
    def twoSum(self, nums, target):
        map={}
        for ind,i in enumerate(nums):
            n=target-i
            if n in map:
                return [map[n], ind]
            map[i]=ind
        