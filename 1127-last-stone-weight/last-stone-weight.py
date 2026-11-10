class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        while len(stones)>1:
            stones.sort()
            lar2= stones.pop()
            lar1= stones.pop()

            if lar1 != lar2:
                stones.append(lar2-lar1)
           
        if stones:
            return stones[0]
        else:
            return 0
        
