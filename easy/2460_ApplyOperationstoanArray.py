class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        insert_pos = 0
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1


        return nums


nums = [1,2,2,1,1,0]

s = Solution()
print(s.applyOperations(nums))