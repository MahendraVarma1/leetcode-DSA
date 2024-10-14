class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        #so all are distinct numbers
        total_sum = n * (n+1) // 2
        actual_sum = sum(nums)
        return total_sum - actual_sum
        
        