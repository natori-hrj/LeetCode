from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        line = [0] * (n + 1)

        for l, r in queries:
            line[l] += 1
            if r + 1 < n:
                line[r + 1] -= 1

        total_decrement = 0
        for i in range(n):
            total_decrement += line[i]
            if total_decrement < nums[i]:
                return False

        return True
