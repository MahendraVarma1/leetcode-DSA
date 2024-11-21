class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        len1 = len(words) 
        dict1 = {}

      
        for char in words[0]:
            dict1[char] = dict1.get(char, 0) + 1

    
        for i in range(1, len1):
            temp_dict = {}
            for char in words[i]:
                if char in dict1 and dict1[char] > 0:
                    temp_dict[char] = temp_dict.get(char, 0) + 1
                    dict1[char] -= 1 
            dict1 = temp_dict 

      
        result = []
        for key, value in dict1.items():
            result.extend([key] * value)  

        return result
        
        
                    
        
        