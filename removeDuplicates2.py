#Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        count = 1
        i = 1
        for j in range(1, len(nums)):
            if nums[j] == nums[j-1]:
                if i<2:
                    nums[count] = nums[j]
                    count = count + 1
                    i = i + 1
            else:
                nums[count] = nums[j]
                count = count + 1
                i = 1
        return count
