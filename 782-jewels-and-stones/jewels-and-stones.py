class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        return sum(1 for i in stones if i in jewels)