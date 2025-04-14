class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even = (n + 1) // 2
        odd = n // 2

        def modpow(a, b):
            res = 1
            a %= MOD
            while b:
                if b % 2:
                    res = (res * a) % MOD
                a = (a * a) % MOD
                b //= 2
            return res

        return (modpow(5, even) * modpow(4, odd)) % MOD
