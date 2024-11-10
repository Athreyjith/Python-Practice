age = int (input( " enter your age  "))

if age >= 18 :
    print(" you r welcome")
elif age <= 0 :
    print (" you r not born ")
else:
    print(" sorry no")


response  = input (" do u like food say (Y/N)")

if response == "Y":
    print(" you like food")
elif response == 'X':
    print("you dont like food")
else:
    print(" your input should be Y or N")


NAME = input("enter your name ")
if NAME == '':
    print(" u didnt type your name")
else :
    print(f"hello {NAME}")


# using boolean
online = False
if online :
    print("user is online")
else :
    print(f" ur is not online")