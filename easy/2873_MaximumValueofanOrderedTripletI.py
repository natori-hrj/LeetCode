class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0

        for j in range(1, n - 1):
            max_i = max(nums[:j]) 
            for k in range(j + 1, n):
                value = (max_i - nums[j]) * nums[k]
                res = max(res, value)

        return max(res, 0)