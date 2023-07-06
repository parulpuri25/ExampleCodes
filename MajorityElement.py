#Given an array nums of size n, return the majority element.
def majorityElement(nums):
    count = {}
    res, maxCount = 0, 0
    for i in nums:
        count[i] = 1 + count.get(i, 0)
        if count[i] > maxCount:
            res = i
            maxCount = count[i]
    return res
