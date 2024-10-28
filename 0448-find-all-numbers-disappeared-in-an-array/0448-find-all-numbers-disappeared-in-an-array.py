class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dict = {}
        list1 = []
        nums.sort()
        for i in range(1,len(nums)+1):
            dict[i] = 0
        num = 0
        for i in nums:
            if num in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        for i in dict:
            if dict[i] == 0:
                list1.append(i)
        return list1
            
                
        