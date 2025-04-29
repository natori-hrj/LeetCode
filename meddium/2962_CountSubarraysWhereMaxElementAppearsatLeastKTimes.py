class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        res = 0
        max_val = max(nums)
        count = 0
        left = 0

        for right in range(n):
            if nums[right] == max_val:
                count += 1

            while count >= k:
                res += n - right
                if nums[left] == max_val:
                    count -= 1
                left += 1

        return res
