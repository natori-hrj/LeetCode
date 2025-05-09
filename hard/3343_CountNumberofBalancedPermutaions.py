from functools import cache
from collections import Counter
from math import comb

MOD = 10**9 + 7

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        nums = list(map(int, num))
        total_sum = sum(nums)
        n = len(nums)

        if total_sum % 2 != 0:
            return 0

        target = total_sum // 2
        count = Counter(nums)

        @cache
        def dfs(digit: int, remain_sum: int, even_slots: int, odd_slots: int) -> int:
            if digit > 9:
                return int((remain_sum == 0) and (even_slots == 0) and (odd_slots == 0))

            if even_slots == 0 and remain_sum > 0:
                return 0

            res = 0
            for left in range(min(count[digit], even_slots) + 1):
                right = count[digit] - left
                if 0 <= right <= odd_slots and digit * left <= remain_sum:
                    ways = comb(even_slots, left) * comb(odd_slots, right)
                    res = (res + ways * dfs(digit + 1, remain_sum - digit * left, even_slots - left, odd_slots - right)) % MOD
            return res

        return dfs(0, target, n // 2, (n + 1) // 2)
