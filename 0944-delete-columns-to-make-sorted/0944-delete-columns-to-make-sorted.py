class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(
            any(strs[row][col] < strs[row - 1][col] for row in range(1, len(strs)))
            for col in range(len(strs[0]))
        )
        
        
            
            
            
            
            
        
        
        