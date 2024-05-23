#
# print("global variables:",globals())
#
# print("global variables:",locals())
#
# a=10
# b=20
#
# # print("after global variables:",globals())
# #
# # print("after global variables:",locals())
#
# def fun1():
#     c=30
#     d=40
#     e=50
#     print("local inside fun1:",locals())
#     print("global inside fun1:", globals())
#     return c
#     return d
#     return e
# d=fun1()
# print("d value outside fun1:",d)
# print("a value outside fun1:",a)
#
#
# fun1=fun1()
# print(fun1)
#
# f=10
# def add():
#     return 0
#
# def outer_func():
#     out_var1=10
#     out_var2="spark"
#     print("local inside outer_func:",locals())
#     print("golbal inside outer_func:", globals())
#     return out_var1,out_var2
# outer_func()
#
#     def inner_func():
#        in_var1=110
#        in_var2='pyspark'
#        print("local inside inner_func:",locals())
#        print("global inside inner_func:",globals())
#        return in_var1,in_var2
#    inner_func()
#
# ---------------------------------
def outer_func():
    outer_var = "outer123"


    def inner_func():
        inner_var = 30
        print("local objects inside inner fun", locals())
        print("globals objects inside inner fun", globals())
        print("outer variable inside inner function",outer_var)  # accessing variable from enclosing
        print("e value is ", e)
    # print(inner_var)
    e=55
    print("local objects inside outer fun", locals())
    print("global objects inside outer fun", globals())
    inner_func()


outer_func()