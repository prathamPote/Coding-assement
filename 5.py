lb = int(input("Enter the lower bound"))
ub = int(input("Enter the upper bound"))
list =[]
flag=0
for i in range(lb,ub+1):
    if i>0:
        for j in range(2,i-1):
            if(i%j)==0:
                print("not prime")
                flag=1
                break
    if flag==0:
        print(i)

print("The prime numbers between",lb,"and ",ub,"are :",list)