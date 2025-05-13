class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        n = len(digits)
        evens = set()
        for i in range(n):
            d1 = digits[i]
            if d1 == 0:  # no leading zeros
                continue
            for j in range(n):
                if j == i:
                    continue
                d2 = digits[j]
                for k in range(n):
                    if k == i or k == j:
                        continue
                    d3 = digits[k]
                    if d3 % 2 != 0:
                        continue
                    num = d1 * 100 + d2 * 10 + d3
                    evens.add(num)
        return sorted(evens)
