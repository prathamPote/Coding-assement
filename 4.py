n = int(input("Enter the value of n"))
for i in range(0,n):
    num =1
    for j in range(0,i+1):
        print(num,end="")
        num+=1
    for k in range(i,0,-1):
            print(k,end="")
    print("\r")
