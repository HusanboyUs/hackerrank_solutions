l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

num = ''.join(map(str,l1))[::-1]
num2=''.join(map(str,l2))[::-1]

print(num)
print(num2)

total = int(num) + int(num2)

result = list(str(total))
print(result)