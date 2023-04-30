n = int(input("enter your number.\n"))
fact=1
if n<0:
    print("The factorial is not possible due to negative values.")
elif n==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,n+1):
        fact = fact*i
    print(f"The factorial of {n} is {fact}")
