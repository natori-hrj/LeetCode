class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        n = len(nums)
        max_right = [0] * n
        max_right[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], nums[i])

        max_val = 0
        max_left = nums[0]

        for j in range(1, n - 1):
            if max_left > nums[j]:
                candidate = (max_left - nums[j]) * max_right[j + 1]
                max_val = max(max_val, candidate)
            max_left = max(max_left, nums[j])

        return max_val
