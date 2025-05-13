class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        dp = [1] * 26
        
        for _ in range(t):
            next_dp = [0] * 26
            for c in range(25):
                next_dp[c] = dp[c+1]
            next_dp[25] = (dp[0] + dp[1]) % MOD
            dp = next_dp
        
        ans = 0
        for ch in s:
            ans = (ans + dp[ord(ch) - ord('a')]) % MOD
        return ans
