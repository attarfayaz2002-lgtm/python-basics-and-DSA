def Linear_Search(nums,n,k):
    n=len(nums)
    i=0
    while i<n:
        if(nums[i]==k):
            return i
        else:
            i+=1
    return -1
n=int(input("Enter the number of elements in the array:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the  element:")))
key=int(input("Enter the element to sarch in the array:"))
result=Linear_Search(arr,n,key)
if result!=-1:
    print("Element found at index:"+ str(result))
else:
    print("Element does not exist in the array")
    
