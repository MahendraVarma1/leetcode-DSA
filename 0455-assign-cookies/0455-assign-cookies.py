class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  
        s.sort()  
        
        child_i = 0  
        cookie_j = 0 
        count = 0
        
       
        while child_i < len(g) and cookie_j < len(s):
           
            if s[cookie_j] >= g[child_i]:
                count += 1  
                child_i += 1  
            
            cookie_j += 1
        
        return count
        