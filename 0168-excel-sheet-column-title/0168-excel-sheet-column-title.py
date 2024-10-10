class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        '''
        if columnNumber >= 2**31 - 1 :
            return 0
        remainder = columnNumber % 26
        quotient = columnNumber // 26
        if columnNumber <= 26:
            return chr(64+columnNumber)
        else:
            return chr(64+quotient)+chr(64+remainder)
        The above code runs for every test case except one
        '''
        result = []
        
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            result.append(chr(65 + remainder))  
            columnNumber //= 26  
        return ''.join(result[::-1])
        
        