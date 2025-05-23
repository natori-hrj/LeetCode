class Solution:
    def triangleType(self, nums: list[int]) -> str:
        a, b, c = sorted(nums)
        if a + b <= c:
            return "none"
        if a == b == c:
            return "equilateral"
        if a == b or b == c:
            return "isosceles"
        return "scalene"
