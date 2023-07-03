#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
def rotate(nums,k):
  nums.reverse()
  nums[:k] = reversed(nums[:k])
  nums[k:] = reversed(nums[k:])
  return nums

print(rotate([1,2,3,4,5,6,7],2)
      
