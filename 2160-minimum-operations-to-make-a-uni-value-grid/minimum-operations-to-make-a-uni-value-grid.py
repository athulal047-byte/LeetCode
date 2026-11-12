class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        ngrid=[]
        for i in grid:
            for item in i:
                ngrid.append(item)

        ngrid.sort()
        rem=ngrid[0]%x
        res=0
        mid = ngrid[len(ngrid)//2]
        for i in ngrid:
            if i%x != rem:
                return -1
            res = res+abs(mid - i) //x

        return res
        