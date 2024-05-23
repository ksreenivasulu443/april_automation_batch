# print(len("Mehboob"))
# print(len)
#
# a = 10
# b = 20
#
# print("a value is ",a)
# print("b value is ",b)
#
# print("after a n b creation all global objects",globals())
# print("after a n b creation all local objects",locals())
#
# def calc():
#     c=30
#     d=10
#     print("global variable inside the cal function",globals())
#     print("local variable inside the cal function",locals())
#
# c=calc()

def outer_fun():
    a=10
    print("a value inside the outer function",a)

    def inner_fun():
        a=11
        print("a value is ",a)
        print(globals())
        print(locals())
        a=12
        print("a value is ",a)
    inner_fun()

outer_fun()