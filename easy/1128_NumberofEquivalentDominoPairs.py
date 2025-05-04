class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        from collections import Counter

        counter = Counter()
        for a, b in dominoes:
            key = tuple(sorted((a, b)))
            counter[key] += 1

        ans = 0
        for count in counter.values():
            ans += count * (count - 1) // 2

        return ans
