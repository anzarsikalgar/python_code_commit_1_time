n = int(input("enter your number.\n"))
def factorial(m):
    if(m==0 or m==1):
        return 1
    else:
        return m*factorial(m-1)
print(f"The factorial of {n} is:",factorial(n))

