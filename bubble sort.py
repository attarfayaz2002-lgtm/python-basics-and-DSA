li=[4,5,1,3,2]
n=len(li)
for i in range(n):
    for j in range(n-i-1):
        if(li[j]>li[j+1]):
            li[j],li[j+1]=li[j+1],li[j]
print(li)
