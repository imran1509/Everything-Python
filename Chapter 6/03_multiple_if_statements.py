b = int(input("Enter your age: "))

# If statement no. 1
if(b%2==0):
    print("b is even")

# End of If statement no. 1

# If staement no. 2
if(b>=18):
    print("you are above the age of consent")

elif(b<=0):
    print("you are entering an invalid age")

else:
    print("you are below the age of consent")

# End of If statement no. 2

print("End of program")