'''
In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
'''

if __name__ == '__main__':
    s = input()

    print(any([s.isalnum() for s in s]))
    print(any([s.isalpha() for s in s]))
    print(any([s.isdigit() for s in s]))
    print(any([s.islower() for s in s]))
    print(any([s.isupper() for s in s]))   



    

