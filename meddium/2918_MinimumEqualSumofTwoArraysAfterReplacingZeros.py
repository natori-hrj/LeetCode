class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        zeros1, zeros2 = nums1.count(0), nums2.count(0)

        
        min_fill1 = sum1 + zeros1
        min_fill2 = sum2 + zeros2

        if zeros1 == 0 and sum1 < min_fill2:
            return -1
        if zeros2 == 0 and sum2 < min_fill1:
            return -1

        return max(min_fill1, min_fill2)