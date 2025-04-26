class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        res = 0
        minPos = maxPos = badPos = -1

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                badPos = i
            if num == minK:
                minPos = i
            if num == maxK:
                maxPos = i
            res += max(0, min(minPos, maxPos) - badPos)

        return res
