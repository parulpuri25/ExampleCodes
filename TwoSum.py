#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#Simple Solution
  def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

#Optimal Solution - Use Hash Map
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in answer:
                return answer[diff],i
            else:
                answer[nums[i]] = i
