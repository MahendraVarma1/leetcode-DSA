class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        ''''max_sum = 0
        for i in range(len(nums)):
            result = 0
            for j in range(i + 1, len(nums)):
                result += min(nums[i], nums[j])
            if max_sum < result:
                max_sum = result
        return result'''
        nums.sort()
        return sum(nums[i] for i in range(0, len(nums), 2))
        