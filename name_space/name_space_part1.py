# print(len("sreeni"))
# print(len)
#
# print(" before a & b creation all global objects", globals())
# print(" before a & b creation all local objects", locals())
# a = 10
# b = 20
#
# print("a value is ", a)
# print("b value is ", b)
#
# print("after a & b creation all global objects", globals())
# print("after a & b creation all global objects", locals())
#
#
# def cal():
#     f = 100
#     c = 30
#     d = 40
#     print("global variables inside cal function", globals())
#     print("local variables inside cal function", locals())
#     print("c value is", c)
#     print("a value inside the cal function", a)
#     return c
#
#
# c = cal()
#
# print("c value is ouside cal fun ", c)
# print("a value outside the cal function", a)

# g = 10
#
# def add():
#     return 0
#
# def outer_func():
#     outer_var = "outer123"
#
#
#     def inner_func():
#         inner_var = 30
#         print("local objects inside inner fun", locals())
#         print("globals objects inside inner fun", globals())
#         print("outer variable inside inner function",outer_var)  # accessing variable from enclosing
#         print("e value is ", e)
#     # print(inner_var)
#     e=55
#     print("local objects inside outer fun", locals())
#     print("global objects inside outer fun", globals())
#     inner_func()
#
#
# outer_func()
#
# # print(outer_var)


def outer_fun():
    a = 11
    global b
    b=20
    print("a value inside outer fun", a)

    def inner_fun():
        a = 12
        print("a value is ", a)
        print(globals())
        print(locals())
        a = 13
        print("a value is ", a)

    inner_fun()


outer_fun()
print("a value ouside fun", b)
