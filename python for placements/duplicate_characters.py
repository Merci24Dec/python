#To get the duplicate characters of a string by ignoring cases

print("Enter a string: ")
st=input()
st=st.lower()
L= len(st)
print("duplicate characters are")
for i in range(0,L):
    count=1
    for j in range(i+1,L):
        if(st[i]==st[j] and st[i]!=' '):
            count=count+1
     #Set string[j] to \0 to avoid printing visited character
            st= st[ :j]+ '\0'+ st[j+1:] 
    if(count>1 and st[i]!='\0'):
        print(st[i],end=" ")
#o/p
"""
Enter a string: 

akash

duplicate characters are

a 
"""
