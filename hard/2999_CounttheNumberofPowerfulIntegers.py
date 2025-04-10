class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        m = len(s)
        t = 10 ** m      
        r = int(s)       
        
        if finish < r:
            return 0

        L0 = 0 if start <= r else (start - r + t - 1) // t
        U0 = (finish - r) // t
        if U0 < L0:
            return 0

        if limit == 9:
            return U0 - L0 + 1

        return self.countValid(U0, limit) - self.countValid(L0 - 1, limit)
    
    def countValid(self, x: int, limit: int) -> int:
        if x < 0:
            return 0
        s = str(x)
        n = len(s)
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def dp(pos: int, tight: bool, started: bool) -> int:
            if pos == n:
                return 1
            res = 0
            up = int(s[pos]) if tight else 9
            for d in range(0, up + 1):
                if d > limit:
                    break  
                ntight = tight and (d == up)
                nstarted = started or (d != 0)
                res += dp(pos + 1, ntight, nstarted)
            return res
        
        return dp(0, True, False)
