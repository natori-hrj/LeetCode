class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        import bisect

        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n):
            l = bisect.bisect_left(nums, lower - nums[i], i + 1)
            r = bisect.bisect_right(nums, upper - nums[i], i + 1)
            count += r - l

        return count
