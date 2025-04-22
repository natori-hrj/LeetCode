class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        from math import comb
        MOD = 10**9 + 7
        max_len = 14

        dp = [[0] * (max_len + 1) for _ in range(maxValue + 1)]
        for i in range(1, maxValue + 1):
            dp[i][1] = 1

        for l in range(2, max_len + 1):
            for i in range(1, maxValue + 1):
                j = i * 2
                while j <= maxValue:
                    dp[j][l] = (dp[j][l] + dp[i][l - 1]) % MOD
                    j += i

        res = 0
        fact = [1] * (n + 1)
        inv = [1] * (n + 1)

        # 階乗・逆元の事前計算（modinv）
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, 0, -1):
            inv[i] = inv[i + 1] * (i + 1) % MOD

        def comb_mod(a, b):
            if a < b:
                return 0
            return fact[a] * inv[b] % MOD * inv[a - b] % MOD

        for i in range(1, maxValue + 1):
            for l in range(1, max_len + 1):
                if dp[i][l]:
                    res = (res + dp[i][l] * comb_mod(n - 1, l - 1)) % MOD

        return res
