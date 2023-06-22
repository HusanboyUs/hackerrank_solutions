

def fake_bin(x):
    result=[]

    for ele in list(x):

        if int(ele) < 5:
            result.append(0)
      
        elif int(ele) >= 5:
            result.append(1)
  
    return ''.join(map(str,result))   

print(fake_bin('15889923'))