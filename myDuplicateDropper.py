lister = [1,2,3,4,4,4,5,6,6,6,1,2,7,8,9,6,7,3,2,0]

def myDuplicator(argList):
    li = argList
    result= []
    for ind,x in enumerate(lister):
        for inde,n in enumerate(li):
            if ind == inde and x == n and x not in result:
                result.append(x)

    return result

#print(myDuplicator(lister))
