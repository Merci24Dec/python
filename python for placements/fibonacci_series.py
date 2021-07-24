#fibonacci Series

a=0;b=1
print("Enter a input: ")
n=int(input())
print("The fibonacci series is ")
for i in range(0,n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
#o/p
/*
Enter a input: 

5

The fibonacci series is 

0 1 1 2 3 
*/
