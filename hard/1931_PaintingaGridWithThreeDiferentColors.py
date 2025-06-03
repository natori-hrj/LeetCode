class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        from functools import lru_cache

        MOD = 10**9 + 7

        def is_valid(col):
            for i in range(1, len(col)):
                if col[i] == col[i - 1]:
                    return False
            return True

        def decode(code):
            col = []
            for _ in range(m):
                col.append(code % 3)
                code //= 3
            return tuple(reversed(col))

        valid_cols = []
        for base in range(3**m):
            col = decode(base)
            if is_valid(col):
                valid_cols.append(base)

        adj = {}
        for a in valid_cols:
            adj[a] = []
            a_col = decode(a)
            for b in valid_cols:
                b_col = decode(b)
                if all(x != y for x, y in zip(a_col, b_col)):
                    adj[a].append(b)

        @lru_cache(None)
        def dp(i, last_col):
            if i == n:
                return 1
            res = 0
            for nei in adj[last_col]:
                res = (res + dp(i + 1, nei)) % MOD
            return res

        return sum(dp(1, col) for col in valid_cols) % MOD
