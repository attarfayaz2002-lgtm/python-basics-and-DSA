prices=[8,5,6,3,7,5,3,5]
def maxProfit(prices):
 ans=0
 minValueSoFar=prices[0]
 for i in range(1,len(prices)):
     profit=prices[i]-minValueSoFar
     if(profit>ans):
         ans=profit
     if(prices[i]<minValueSoFar):
         minValueSoFar=prices[i]
 return ans
print(maxProfit(prices))
