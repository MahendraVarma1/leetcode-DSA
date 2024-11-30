class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        rank = {value: index for index, value in enumerate(arr2)}

   
        arr1.sort(key=lambda x: (rank.get(x, len(arr2)), x))

        return arr1
        