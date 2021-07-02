#To determine the largest of 4 numbers
a=int(input())
b=int(input())
c=int(input())
d=int(input())

if(a>b and a>c and a>d):
    print(a,'is greater')
elif(b>c and b>d and b>a):
    print(b,'is greater')
elif(c>d and c>a and c>b):
    print(c,'is greater')
else:
    print(d,'is greater')
