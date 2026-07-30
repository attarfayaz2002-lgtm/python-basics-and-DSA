def CompoundInterest(P,N):
    if N==0:
        return 1
    else:
        return P**N
PrincipalRate=int(input("Enter the amount: "))
Year=int(input("Enter the number of years:"))
result=CompoundInterest(PrincipalRate,Year)
print(f"Compound Interest is:{result} Rupees only")
