nums=[0,1,1,1,0,0,1,1]
def consecutiveOnes(nums):
    max_count=0
    current_count=0
    for i in range(len(nums)):
        if(nums[i]==0):
            current_count=0
        else:
            current_count+=1
        if current_count> max_count:
            max_count=current_count
    return max_count
print(consecutiveOnes(nums))
