a = input("Enter the string")
for i in (0,len(a)):
    if i<len(a)-2:
        if(a[i]==a[i+1]):
            if(a[i]==a[i+2]):
                a.replace(a[i+2],"")
print(a)