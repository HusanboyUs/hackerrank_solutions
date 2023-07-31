def mySoltuion(haystack:str,needle):
    result = []
    charRes = []
    final = []
    if needle in haystack:
        for indx,ele in enumerate(list(haystack)):
            for ind,char in enumerate(list(needle)):
                if char == ele:
                    result.append(indx)
                    charRes.append(ele)
                
                                
        print(result)
        print(charRes)   
        
        return result[0]            
    
    else:
        return -1 
      
            

print(mySoltuion('mississippi','issip'))    
