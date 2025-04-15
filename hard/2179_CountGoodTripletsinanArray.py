class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 2)

    def update(self, i, delta):
        i += 1
        while i <= self.n + 1:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

class Solution:
    def goodTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        pos2 = {val: i for i, val in enumerate(nums2)}

        transformed = [pos2[val] for val in nums1]

        bit_left = FenwickTree(n)
        left_smaller = [0] * n

        for i in range(n):
            rank = transformed[i]
            left_smaller[i] = bit_left.query(rank - 1)
            bit_left.update(rank, 1)

        bit_right = FenwickTree(n)
        right_larger = [0] * n
        for i in reversed(range(n)):
            rank = transformed[i]
            right_larger[i] = bit_right.query(n - 1) - bit_right.query(rank)
            bit_right.update(rank, 1)

        ans = 0
        for i in range(n):
            ans += left_smaller[i] * right_larger[i]

        return ans
