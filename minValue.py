#Find Minimum Value in list
def findMin(self, nums: List[int]) -> int:
        min_val = nums[0]
        for i in range(1,len(nums)):
            if min_val > nums[i]:
                min_val = nums[i]
        return min_val

