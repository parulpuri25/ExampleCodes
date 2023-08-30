def searchInsert(nums,target):
    start,end= 0,len(nums)-1
    while(end>=start):
        mid = (start + end)//2
        if(nums[mid] == target):
            return mid
        elif(target>nums[mid]):
            start = mid+1
        elif(target<nums[mid]):
            end= mid-1
        return start
