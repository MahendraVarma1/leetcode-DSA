class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        normalized_str = re.sub(r'[^\w\s]', ' ', paragraph).lower()
    
  
        words = normalized_str.split()
    

        banned_set = set(banned)
    
  
        word_counts = Counter(word for word in words if word not in banned_set)
    

        most_common = word_counts.most_common(1)[0][0]
    
        return most_common
        