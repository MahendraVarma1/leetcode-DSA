class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, current_combination: List[int], current_sum: int):
            if current_sum == target:
                result.append(list(current_combination))
                return

            if current_sum > target:
                return

            for i in range(start, len(candidates)):
                current_combination.append(candidates[i])
                backtrack(i, current_combination, current_sum + candidates[i])
                current_combination.pop()

        backtrack(0, [], 0)
        return result
        