class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        c_indices = []
        for i in range(len(s)):
            if s[i] == c:
                c_indices.append(i)
        
        result = []
        for i in range(len(s)):
            shortest_distance = min(abs(i - idx) for idx in c_indices)
            result.append(shortest_distance)
        
        return result
        
        