class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        min_sum = max_sum = curr = 0

        for diff in differences:
            curr += diff
            min_sum = min(min_sum, curr)
            max_sum = max(max_sum, curr)

        min_start = lower - min_sum
        max_start = upper - max_sum

        return max(0, max_start - min_start + 1)
