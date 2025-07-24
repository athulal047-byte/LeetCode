class Solution(object):
    def minOperations(self, boxes):
        n=len(boxes)
        answer=[]
        for i in range(n):
            oprs=0
            for j in range(n):
                if boxes[j]=='1':
                    oprs += abs(i-j)
            answer.append(oprs)
        return answer