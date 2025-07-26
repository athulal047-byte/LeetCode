class Solution(object):
    def convertTemperature(self, celsius):
        list=[]
        list.append(celsius + 273.15)
        list.append(celsius * 1.80 + 32.00)
        return list