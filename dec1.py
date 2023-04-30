def decor1(num):
    def inner():
        b=num()
        multi=b*5
        return multi
    return inner

def decor(num):
    def inner():
        a=num()
        add=a+5
        return add
    return inner
def num():
    n = int(input("enter your number.\n"))
    return n
num = decor(decor1(num))
print(num())

