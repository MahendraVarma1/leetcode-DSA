class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        element_info = {}
        
        
        for i, num in enumerate(nums):
            if num in element_info:
                element_info[num][0] += 1  
                element_info[num][2] = i   
            else:
                element_info[num] = [1, i, i]  
        
    
        degree = max(info[0] for info in element_info.values())
        
       
        min_length = float('inf')
        
    
        for freq, first, last in element_info.values():
            if freq == degree:
                min_length = min(min_length, last - first + 1)
        
        return min_length
            
        
            
            
        