from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [1] * n
        prev = [-1] * n

        def hamming1(a: str, b: str) -> bool:
            diff = 0
            for ca, cb in zip(a, b):
                if ca != cb:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1

        best_end, best_len = 0, 1
        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] \
                   and len(words[i]) == len(words[j]) \
                   and hamming1(words[i], words[j]):
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > best_len:
                best_len = dp[i]
                best_end = i

        res = []
        cur = best_end
        while cur != -1:
            res.append(words[cur])
            cur = prev[cur]
        return res[::-1]
