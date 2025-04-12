class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        import math
        import collections
        half = (n + 1) // 2
        start = 10 ** (half - 1)
        end = 10 ** half
        seen = set()
        total = 0

        for x in range(start, end):
            s = str(x)
            pal = s + s[::-1][n % 2:]

            if int(pal) % k != 0:
                continue

            key = ''.join(sorted(pal))
            if key in seen:
                continue
            seen.add(key)

            counter = collections.Counter(pal)

            leading = n - counter['0']
            ways = leading * math.factorial(n - 1)

            for freq in counter.values():
                ways //= math.factorial(freq)

            total += ways

        return total
