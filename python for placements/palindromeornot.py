#Program to check whether a string or number is palindrome or not
print ("Enter a string:") 
st = input ()
rev = st[: :-1] 
if (st == rev):
  print ("The string is pallindrome")
else:
  print ("The string is not a pallindrome")
#o/p
"""
Enter a string:

akash

The string is not a pallindrome
"""
