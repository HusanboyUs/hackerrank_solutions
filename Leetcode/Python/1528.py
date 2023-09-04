s = "codeleet"
indices = [4,5,6,7,0,2,1,3]


#expected leetcode
'''
for indx in indices:
    print(s[indx])
'''


def shuffleString(s,indices):
    result =[]
    temp = {indices[i]:s[i] for i in range(len(indices))}
    sorted_temp = dict(sorted(temp.items(), key=lambda item: item[1]))


    
    return sorted_temp

print(shuffleString(s,indices))    