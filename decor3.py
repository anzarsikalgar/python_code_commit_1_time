def check(func):
    def wrap(a,b):
        if a>b:
            print(a,"is greater than",b)
            return func(a,b)
        else:
            print(b,"is greater than",a)
            return func(b,a)
    return wrap
@check
def sub(x,y):
    return x-y
print("The substraction of numbers :",sub(8,10))
 