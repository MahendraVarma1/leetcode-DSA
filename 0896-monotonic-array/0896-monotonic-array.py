class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_increasing = all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))
    
        is_decreasing = all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))
    
        return is_increasing or is_decreasing
            
            
            
        