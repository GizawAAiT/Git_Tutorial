def missingNumber( nums):
    nums.append(-1) 
    
    def cycle_sort():
        for indx in range(len(nums)):
            while nums[indx] != indx : 
                if nums[indx] == -1: break
                nums[nums[indx]], nums[indx] = nums[indx], nums[nums[indx]]
    
    cycle_sort()
    
    for i in range(len(nums)):
        if nums[i] == -1:
            return i 
    return nums
print(missingNumber([3, 0, 1])) # output: 2

