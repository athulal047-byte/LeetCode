class Solution(object):
    def isPalindrome(self, s):
        
        s=s.lower()
        r=""
        for i in s:
            if i.isalnum():
                r = r + i
        s=r[::-1]
        if s==r:
            return True
        else:
            return False
        
        