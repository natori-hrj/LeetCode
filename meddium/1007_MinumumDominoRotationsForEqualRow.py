class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        def check(x):
            rotations_top = rotations_bottom = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return float('inf')
                elif tops[i] != x:
                    rotations_top += 1
                elif bottoms[i] != x:
                    rotations_bottom += 1
            return min(rotations_top, rotations_bottom)

        candidates = [tops[0], bottoms[0]]
        res = min(check(c) for c in candidates)
        return res if res != float('inf') else -1
