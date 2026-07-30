def Search(list,Search_element):
    n=len(list)
    i=0
    while i<=n:
        if(list[i]==Search_element):
            return i
        else:
            i+=1
    return -1
E_ID=[15,10,25,20,40]
key=int(input("Enter the Employee ID you want to search:"))
index =Search(E_ID,key)
print(index)
if index!=-1:
    print(f"The Employee_ID is at index{index}")
else:
    print("The given Employee_ID is invalid")
