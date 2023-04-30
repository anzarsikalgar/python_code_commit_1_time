def check(func):
    def inner(a,b):
        if a>b:
            print(a,"is greater than:",b)
            return func(a,b)
        else:
            print(b,"is greater than:",a)
            return func(b,a)
    return inner

@check
def sub(x,y):
    return x-y
n1 = int(input("enter your 1st no.\n"))
n2 = int(input("enter your 2nd no.\n"))
print("The substraction of numbers\n: ", sub(n1,n2))
