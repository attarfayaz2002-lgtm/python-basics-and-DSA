li =[5,4,9,3,1,8]
n=len(li)
print("Before Selecting"+str(li))
for i in range(n):
    smallIndex=i
    for j in range(i,n):
        if(li[j]< li[smallIndex]):
            smallIndex = j
    print("After Selecting"+ str(li[smallIndex])+ "at index" + str(i))
    li[i],li[smallIndex]=li[smallIndex],li[i]
print(str(li))            
