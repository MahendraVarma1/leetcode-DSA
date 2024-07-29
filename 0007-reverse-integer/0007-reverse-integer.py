class Solution:
    def reverse(self, x: int) -> int:
        temp = str(x)
        if x<0:
            temp = -int(str(-x)[::-1])
        else:
            temp = int(str(x)[::-1])
        if temp < -2**31 or temp > 2**31 - 1:
            return 0
        return temp
        
            
        