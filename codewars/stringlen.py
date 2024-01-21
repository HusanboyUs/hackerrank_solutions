

name = 'husanghost'

counter = 0
for x in range(len(name)):
    print(name[0:counter+1])
    counter +=1

counter = len(name)
for x in range(len(name)):
    print(name[0:counter-1])
    counter -=1