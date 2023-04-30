p = int(input("enter your number.\n")) 
if p<0:
    print("Negative value is not possible.")
else:
    def fact(r):
        if(r ==0 or r==1):
            return 1
        else:
            return r*fact(r-1)
    result =fact(p) 
    print(f"The factorial of {p} is {result}")
