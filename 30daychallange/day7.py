# Enter your code here. Read input from STDIN. Print output to STDOUT
number=2
my_string='Hacker'
s='Rank'


my_words=my_string,s
count=0

right=''
left=''

while len(my_words) != count:
    for indx,char in enumerate(my_words[count]):
        if indx%2==0:
            right=right+char
        elif indx%2!=0:
            left = left+char
    print(right+" "+left)        
    count += 1
    right=""
    left=""



        
    
        


