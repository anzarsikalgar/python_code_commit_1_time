def decor(printer):
    def inner():
        printer()
        print("welcome decor!")
    return inner
@decor
def printer():
    print("welcome1!")
    print("welcome2!")
printer()

    