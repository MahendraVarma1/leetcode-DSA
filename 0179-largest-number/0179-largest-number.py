class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        nums.sort(key=cmp_to_key(compare))
        
        largest_num = ''.join(nums)
        
        return '0' if largest_num[0] == '0' else largest_num
        