class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #frequency_dict = {i: 0 for i in range(10)}
        #frequency_dict = defaultdict(int)
        #for num in nums:
        #    if num in frequency_dict:
        #        frequency_dict[num] += 1
        #for num,count in frequency_dict.items():
        #    if count == 1:
        #        return num
        result = 0
        for num in nums:
            result ^= num
        return result
        
        
        
        
        
        
        