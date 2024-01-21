

def length_of_last_word(word):
    length = 0
    index = len(word) -1
    while index >=0 and word[index] == ' ':
        index -=1
    while index >=0 and word[index] != ' ':
        index -=1
        length +=1
    
    return length



print(length_of_last_word('   fly me   to   the moon  '))