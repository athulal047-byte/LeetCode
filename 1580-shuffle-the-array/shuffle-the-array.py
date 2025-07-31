class Solution(object):
    def shuffle(self, nums, n):
        list=[]
        f=2*n
        g=n+1
        for i in range(n):
            list.append(nums[i])
            list.append(nums[i+n])
        return list
        