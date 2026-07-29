def reverse(nums,start,end):
    i=start
    j=end
    while(i<j):
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
        j-=1
def rotate(nums,k):
    n=len(nums)
    k=k%n
    reverse(nums,0,n-1)
    reverse(nums,0,k-1)
    reverse(nums,k,n-1)
nums=[1,2,3,4,5,6,7]
k=8
rotate(nums,k)
print(nums)
