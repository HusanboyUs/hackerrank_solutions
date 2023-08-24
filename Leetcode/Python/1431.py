candies = [12,1,12]
extraCandies = 10


def solveCandies(candies,extraCandies):
    result = []
    totals = []

    for ele in candies:
        totals.append(ele + extraCandies)

    smallest = min(totals)
    print(smallest)
    print(totals)
    for x in totals:
        if x != smallest:
            result.append(True)
        else:
            result.append(False)    

    return result        
                  

print(solveCandies(candies,extraCandies))    