class Solution:
    def smallestTrimmedNumbers(self, nums: list[str], queries: list[list[int]]) -> list[int]:
    
        maxlen=len(nums[0])
        n=len(nums)

        ordertrim={}
        order = list(range(len(nums)))
        for trim in range(1,maxlen+1):
            dig = maxlen -trim

            order.sort(key=lambda idx: nums[idx][dig])
            ordertrim[trim] = list(order)
    
        ans = []
        for k, trim in queries:
            ans.append(ordertrim[trim][k - 1])
                
        return ans

            