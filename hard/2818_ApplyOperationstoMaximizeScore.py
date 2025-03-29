class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        from collections import defaultdict
        from math import log2

        MOD = 10 ** 9 + 7

        n = len(nums)
        max_val = max(nums)


        spf = list(range(max_val + 1))
        for i in range(2, int(max_val ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        def prime_score(x):
            seen = set()
            while x > 1:
                seen.add(spf[x])
                x //= spf[x]
            return len(seen)

        scores = [prime_score(num) for num in nums]


        left = [0] * n
        right = [0] * n

        stack = []
        for i in range(n):
            while stack and scores[stack[-1]] < scores[i]:
                stack.pop()
            left[i] = i - (stack[-1] if stack else -1)
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and scores[stack[-1]] <= scores[i]:
                stack.pop()
            right[i] = (stack[-1] if stack else n) - i
            stack.append(i)


        freq = [left[i] * right[i] for i in range(n)]

        data = sorted(zip(nums, freq), key=lambda x: -x[0])

        res = 1
        for val, count in data:
            use = min(k, count)
            res = res * pow(val, use, MOD) % MOD
            k -= use
            if k == 0:
                break

        return res