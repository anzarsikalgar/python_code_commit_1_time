l = int(input("enter your number:\n"))
u = int(input("enter your number:\n"))
for n in range(l,u+1):
    count=0
    for i in range(2,n+1):
        if n%i==0:
            count= count+1           
    if count==2:
        print(n)

