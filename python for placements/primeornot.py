#Python program to check whether a number is prime or Not

print("Enter a integer: ")
n=int(input())
flag=1
for i in range(2,(n//2)+1):
    if(n%i==0):
        flag=0
        break

if(flag==1):
    print('{0} is a prime number'.format(n))
else:
    print('{0} is not a prime number'.format(n))
#o/p
"""
Enter a integer: 

25

25 is not a prime number
"""
