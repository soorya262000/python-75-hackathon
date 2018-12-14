x=10
def fun1():
    #"x=x+1"
    print("x=x+1 this statement produces error as this function treats x as a local variable")
def fun2():
    global x
    x=x+1
    print(x)
fun1()
fun2()
