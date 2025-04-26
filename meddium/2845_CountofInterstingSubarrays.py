class Solution:
    def countInterestingSubarrays(self, nums: list[int], modulo: int, k: int) -> int:
        from collections import defaultdict
        count = 0
        prefix = 0
        counter = defaultdict(int)
        counter[0] = 1

        for num in nums:
            if num % modulo == k:
                prefix += 1
            prefix %= modulo

            target = (prefix - k + modulo) % modulo
            count += counter[target]

            counter[prefix] += 1

        return count
