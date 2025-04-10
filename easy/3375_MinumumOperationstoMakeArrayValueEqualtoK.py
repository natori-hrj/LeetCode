class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        if any(x < k for x in nums):
            return -1

        ops = 0

        while not all(x == k for x in nums):
            curr_max = max(nums)

            if curr_max == k:
                break

            found = False

            for h in range(k, curr_max):
                candidates = [x for x in nums if x > h]
                if candidates and len(set(candidates)) == 1:
                    val = candidates[0]
                    nums = [h if x == val else x for x in nums]
                    ops += 1
                    found = True
                    break

            if not found:
                return -1
        return ops
