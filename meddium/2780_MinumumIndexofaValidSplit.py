class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        from collections import Counter

        counter = Counter(nums)
        dominant, total = max(counter.items(), key=lambda x: x[1])

        count = 0
        n = len(nums)

        for i in range(n - 1):
            if nums[i] == dominant:
                count += 1

            if count * 2 > i + 1 and (total - count) * 2 > n - i - 1:
                return i
            
        return -1

nums = [1,2,2,2]
s = Solution()
print(s.minimumIndex(nums))
