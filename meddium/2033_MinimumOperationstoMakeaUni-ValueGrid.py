class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        nums = [num for row in grid for num in row]
        base = nums[0]

        for num in nums:
            if (num - base) % x != 0:
                return -1
            
        nums = [(num - base) // x for num in nums]
        nums.sort()
        median = nums[len(nums) // 2]

        return sum(abs(num - median) for num in nums)

grid = [[2, 4], [6, 8]]
x = 2

s = Solution()
print(s.minOperations(grid, x))