def maxProductArray(nums):
    result=nums[0]
    maxProduct=nums[0]
    minProduct=nums[0]
    for i in range(1,len(nums)):
        if nums[i]>=0:
            maxProduct=max(maxProduct*nums[i],nums[i])
            minProduct=min(minProduct*nums[i],nums[i])
        else:
            temp=maxProduct
            maxProduct=max(minProduct*nums[i],nums[i])
            minProduct=min(temp*nums[i],nums[i])

        result=max(result,maxProduct)
    return result
nums=[2,-1,3,4,5]
print(maxProductArray(nums))
