class Solution(object):
    def convertDateToBinary(self, date):
        list=[]
        return '-'.join(bin(int(i))[2:] for i in date.split('-'))