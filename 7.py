link="Home"
while (1):
    command =input("Enter the command")
    if command == "forward":
        if link == "Home":
             print("Home")
        else:
            print(link)
    if command == "goto":
        link= input()
        print(link)
    if command == "backward":
        if(link!="Home"):
            print(link)
        else:
            print("Home")