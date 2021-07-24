#Swap 2 numbers without using 3rd variable

print("Enter two numbers: ")
a,b= map(int,input().split())
print("Before Swapping")
print("{0} {1}".format(a,b))
a,b=b,a
print("After Swapping")
print("{0} {1}".format(a,b))
#o/p
"""
Enter two numbers: 

51 21

Before Swapping

51 21

After Swapping

21 51
"""
