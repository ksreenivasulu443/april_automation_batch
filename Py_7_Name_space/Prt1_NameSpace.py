
print("before a & b creation Global variables objects", globals())
print("before a & b creation Local variables objects", locals())
a = 10
b = 20

print("a value is", a)
print("a value is", b)

print("after a & b creation Global variables objects", globals())
print("after a & b creation Local variables objects", locals())

def cal():

    f=55
    a = 25
    b = 35
    c = 30
    d = 50
    print("Global variables inside cal function", globals())
    print("Local variables inside cal function", locals())
    print("a value inside the function", a)
    print("b value inside the function", b)


cal()

print("a value outside the function", a)
print("b value outside the function", b)


g = 10

def add():
    return 0


def outer_func():
    outer_var = "outer123"
    print("Global variables inside outer_func", globals())
    print("Local variables inside outer_func", locals())

    def inner_func():
        inner_var =30
        print("Global variables inside inner_func", globals())
        print("Local variables inside inner_func", locals())
        print("outside variable inside inner_func", outer_var)
        e = 55


    inner_func()



outer_func()


a = 10
print("before the function a value is", a)

def outer_fcn():
    a = 12

    def inner_fcn():
        global a
        a = 15
        print("a value is", a)

    inner_fcn()
outer_fcn()
print("after the function a value is", a)