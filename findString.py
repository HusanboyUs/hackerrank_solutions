def count_substring(string, sub_string):
    total = 0
    for i in range(len(string)):
        if string[i: i +len(sub_string) ] == sub_string:
            total+=1
    return total  


          

