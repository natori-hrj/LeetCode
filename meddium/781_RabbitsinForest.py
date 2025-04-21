class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        from collections import Counter
        import math
        
        counter = Counter(answers)
        total = 0

        for x, count in counter.items():
            group_size = x + 1
            group_count = math.ceil(count / group_size)
            total += group_count * group_size

        return total
