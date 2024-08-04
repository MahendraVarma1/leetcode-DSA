from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to use the two-pointer technique
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # Move the left pointer to the right to increase the total
                elif total > 0:
                    right -= 1  # Move the right pointer to the left to decrease the total
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate values for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    # Skip duplicate values for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers
                    left += 1
                    right -= 1
        
        return result
