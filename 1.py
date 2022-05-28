from asyncio.windows_events import NULL


a = int(input("Enter a 5 digit number"))
sum =""
for i in range(5):
    rem = int(a%10)
    rem+=1
    a=a/10 
    sum =sum + str(rem)
tmp=""
sum =tmp.join(reversed(sum))
print(sum)

