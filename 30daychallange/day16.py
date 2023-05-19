S=input()
try:
    strInt=int(S)
    print(strInt)
except ValueError as wrongVal:
    print('Bad String')        