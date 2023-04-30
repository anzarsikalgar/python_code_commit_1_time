num = int(input("enter your number:\n"))
print("prime number : ",end=' ')
for n in range(1,num):
    for i in range(2,n):
        if n%i==0:
            #print(f"{n} is not prime number.")
            break
    else:
        print(n, end=' ')
