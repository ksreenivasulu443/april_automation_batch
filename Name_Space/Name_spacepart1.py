# print(len("Lina"))
# print(len)  # len is built-in function
# print("before a & b creation all global objects", globals())
# print("before a & b creation all local objects", locals())
# a = 10
# b = 20
# print("a value is", a)
# print("b value is", b)
#
# print("after a & b creation all global objects", globals())
# print("after a & b creation all local objects", locals())
#
#
# def cal():
#     global f
#     f = 100
#     c = 30
#     d = 40
#     a = 30
#     print("global variables inside cal function", globals())
#     print("local variables inside cal function", locals())
#     print("C value is", c)
#     print("a value inside the cal function", a)
#     return c
#
#
# c = cal()
# #print(" c value is ", c)  #NameError: name 'c' is not defined here we not define local value out of function body
# print("f of value is", f)  # this is global value ,that's why we print outside the function also
# print("c value outside the function", c)
# print("a value outside the cal function", a)

def add():
    return 0

g = 10
def outer_function():
    outer_var = 'outer'
    print("local objects inside the outer function", locals())
    print("global objects inside the outer function",globals())


outer_function()



