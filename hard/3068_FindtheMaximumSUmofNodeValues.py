class Solution:
    def maximumValueSum(
        self,
        nums: list[int],
        k: int,
        edges: list[list[int]],
    ) -> int:
        xor_values = [num ^ k for num in nums]
        total = 0
        diffs = []

        for original, xor_val in zip(nums, xor_values):
            if xor_val > original:
                total += xor_val
                diffs.append(xor_val - original)
            else:
                total += original
                diffs.append(original - xor_val)

        changed_count = sum(xor_val > num for num, xor_val in zip(nums, xor_values))

        if changed_count % 2 == 0:
            return total
        else:
            min_diff = min(diffs)
            return total - min_diff
