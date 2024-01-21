

prices = [7,1,5,3,6,4]

def maxPrices(prices):
    buy = None
    sell = None

    for stock in range(len(prices)):
        for elem in prices:
            if prices[stock] < elem:
                buy =  prices[stock]
            
            
        
    return buy



print(maxPrices(prices))

