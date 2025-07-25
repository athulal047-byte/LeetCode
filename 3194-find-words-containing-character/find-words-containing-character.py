class Solution(object):
    def findWordsContaining(self, words, x):
        ans=[]
        i=0
        while i < len(words):
            if x in words[i]:
                ans.append(i)
            i +=1
        return ans  
        