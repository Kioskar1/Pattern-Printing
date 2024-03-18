n = int(input('Enter value of n : '))

for i in range(65,66+n):
    for j in range(65,i+1):
        print(chr(j),end='')
    print()