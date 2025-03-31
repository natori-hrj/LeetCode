class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        if k == 1:
            return 0  

        n = len(weights)
        pair_sums = [weights[i] + weights[i+1] for i in range(n - 1)]
        pair_sums.sort()

        max_score = sum(pair_sums[-(k - 1):])
        min_score = sum(pair_sums[:k - 1])

        return max_score - min_score
