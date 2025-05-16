from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)

        def build(start_bit: int) -> List[str]:
            seq = []
            last = None
            bit = start_bit
            for w, g in zip(words, groups):
                if last is None:
                    if g == bit:
                        seq.append(w)
                        last = g
                        bit ^= 1
                else:
                    if g != last:
                        seq.append(w)
                        last = g

            return seq

        seq0 = build(0)
        seq1 = build(1)

        seq2 = []
        last = None
        for w, g in zip(words, groups):
            if last is None or g != last:
                seq2.append(w)
                last = g

        best = max([seq0, seq1, seq2], key=len)
        return best
