l=[]
for n in range(20,50):
    for i in range(2,n):
        if n%i==0:
            #print(f"{n} is not prime number.")
            break
    else:
        l.append(n)
print(l)
