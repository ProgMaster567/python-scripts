a=int(input('Enter the 1st no. of series:'))
b=int(input('Enter the 2nd no. of series:'))
n=int(input('Enter the no. of terms needed:'))
print(a,b,end=' ')
while (n-2):
    c=a-b
    a=b
    b=c
    print(c,end='')
    n=n-1
