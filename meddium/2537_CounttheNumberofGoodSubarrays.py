class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        from collections import defaultdict
        ans = 0
        pairs = 0
        count = defaultdict(int)
        l = 0

        for r in range(len(nums)):
            pairs += count[nums[r]]
            count[nums[r]] += 1

            while pairs >= k:
                count[nums[l]] -= 1
                pairs -= count[nums[l]]
                l += 1

            ans += l

        return ans
