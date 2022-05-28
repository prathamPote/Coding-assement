a =  input("Enter a 4 digit number\n")

for i in range(4):
     if(i==0):
        print(a[i]+"*1000 =",str(int(a[i])*1000))
     if(i == 1):
         print(a[i]+"*100 =",str(int(a[i])*100))
     if(i == 2):
         print(a[i]+"*10 =",str(int(a[i])*10))
     if(i== 3 ):
         print(a[i]+"*1 =",str(int(a[i])*1))