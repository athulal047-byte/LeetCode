class Solution(object):
    def convertDateToBinary(self, date):
        return '-'.join(bin(int(i))[2:] for i in date.split('-'))