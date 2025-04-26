class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        self.total = 0

        def dfs(index, xor_sum):
            if index == len(nums):
                self.total += xor_sum
                return
            
            dfs(index + 1, xor_sum)
            
            dfs(index + 1, xor_sum ^ nums[index])

        dfs(0, 0)
        return self.total