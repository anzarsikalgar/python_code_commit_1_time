n = int(input("enter your number:\n"))
if n>=1:
    for i in range(2,n):
        if n%i==0:
            print(f"{n} is not prime number.")
            break
    else:
        print(f"{n} is prime number.")
else:
    print(f"{n} is not prime number.") 


