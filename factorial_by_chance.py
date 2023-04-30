n = int(input("enter your number.\n"))
fact =1
if n>0:
    for i in range(1,n+1):
        fact=fact*i
    print(f"The factorial of {n} is {fact}")
else:
    print("Not possible for negative.")