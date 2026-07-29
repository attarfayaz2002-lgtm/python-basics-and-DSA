nums=[1,-2,3,-4,6,5]
def maxSubArray(nums):
    current_sum=max_sum=nums[0]
    for num in nums[1:]:
        current_sum=max(num,current_sum+num)
        if current_sum>max_sum:
            max_sum=current_sum
    return max_sum
print(maxSubArray(nums))

