class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  # dp[i] = i番目から最大スコア

        for i in range(n - 1, -1, -1):
            point, skip = questions[i]
            next_index = i + skip + 1
            take = point + (dp[next_index] if next_index < n else 0)
            dp[i] = max(take, dp[i + 1])

        return dp[0]