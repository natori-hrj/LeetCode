class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        MOD = 10**9+7
        M = [[0]*26 for _ in range(26)]
        for p in range(26):
            for k in range(1, nums[p]+1):
                q = (p + k) % 26
                M[p][q] = (M[p][q] + 1) % MOD

        def matmul(A, B):
            C = [[0]*26 for _ in range(26)]
            for i in range(26):
                Ai = A[i]
                Ci = C[i]
                for k, aik in enumerate(Ai):
                    if aik:
                        rowB = B[k]
                        mul = aik
                        for j in range(26):
                            Ci[j] = (Ci[j] + mul * rowB[j]) % MOD
            return C

        # Matrix exponentiation M^e
        def matpow(mat, e):
            # initialize R = I
            R = [[int(i==j) for j in range(26)] for i in range(26)]
            base = mat
            while e > 0:
                if e & 1:
                    R = matmul(R, base)
                base = matmul(base, base)
                e >>= 1
            return R

        Mt = matpow(M, t)
        dp_t = [sum(Mt[p][q] for q in range(26)) % MOD for p in range(26)]

        ans = 0
        o = ord
        for ch in s:
            ans = (ans + dp_t[o(ch)-o('a')]) % MOD
        return ans
