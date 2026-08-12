def Binary_Search(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if(arr[mid]==key):
            return mid
        elif(arr[mid]<key):
            low=mid+1
        else:
            high=mid-1
    return -1
n=int(input("Enter the number of elements:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the element:")))
if arr == sorted(arr):
    print("Array is already sorted")
else:
    print("The array is not sorted")
    print("The array is sorting")
    arr.sort()
print("Sorted list:"+str(arr))
key=int(input("Enter the element to Search:"))
result=Binary_Search(arr,key)
if result!=-1:
    print(f"Element {key} found at index {result}")
else:
    print(f"Element {key} is not present in the list")
    
    
