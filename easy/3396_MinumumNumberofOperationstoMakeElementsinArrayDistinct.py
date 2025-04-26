class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        ops = 0
        start = 0
        n = len(nums)

        while start < n:
            seen = set()
            found_duplicate = False

            for i in range(start, n):
                if nums[i] in seen:
                    found_duplicate = True
                    break
                seen.add(nums[i])

            if not found_duplicate:
                break  # すでに distinct

            # 操作実行：先頭から3つ削除
            ops += 1
            start += 3

        return ops
