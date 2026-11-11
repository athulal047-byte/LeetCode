class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l=0
        lar=0
        win=set()
        for r in range(len(s)):
            
            while s[r] in win:
                win.remove(s[l])
                l += 1
            win.add(s[r])
            w = (r-l) + 1
            lar =max(lar,w)
        return lar   

        