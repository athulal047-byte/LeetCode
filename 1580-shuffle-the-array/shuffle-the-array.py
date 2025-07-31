class Solution(object):
    def shuffle(self, nums, n):
        list=[]
        for i in range(n):
            list.append(nums[i])
            list.append(nums[i+n])
        return list
        