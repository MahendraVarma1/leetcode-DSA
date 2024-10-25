class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        list1 = []
        dict1 = {}
        for item in nums:
            if item in dict1:
                dict1[item] += 1
            else:
                dict1[item] = 1
        for i in dict1:
            if dict1[i] >= k:
                list1.append(i)
        return list1 '''
        frequency_dict = Counter(nums)
        
       
        most_common = frequency_dict.most_common(k)
        
      
        result = [item for item, count in most_common]
        
        return result
                

        
        
        
        
        
        
        
        