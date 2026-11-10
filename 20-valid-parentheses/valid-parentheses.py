class Solution(object):
    def isValid(self, s):
        
        stck=[]
        map={")":"(","}":"{","]":"["}
        for i in s:
            if i in map:
                if not stck:
                    return False
                top=stck.pop()
                if map[i]!= top:
                    return False
            else:
                stck.append(i)
        return len(stck)==0 