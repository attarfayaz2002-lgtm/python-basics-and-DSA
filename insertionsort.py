list = [5,1,4,3,2]
n = len(list)
for i in range(1,n):
    j=i-1
    key=list[i]
    while j>=0 and list[j]>key:
        list[j+1] = list[j]
        j=j-1
    list[j+1]=key
    print(list[:i+1])
print(list)
