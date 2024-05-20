# len('sree')
# print(len)
# print('before a,b creation',globals())
# print('before a,b creation',locals())
# a=20
# b=30
# print('a is',a)
# print('b is',b)
# print('after a,b creation',globals())
# print('after a,b creation',locals())
#
# def cal():
#     a=35
#     c=15
#     d=25
#     global f
#     f=100
#     print('global varibles insde function', globals())
#     print('local varibles insde function', locals())
#     print('a is inside the function',a)
# cal()
# #print('c value ',c) #we cant use loacal varibale in global #if need to use the C value we can Return or change to global
# print('f value ',f) #global varible can be used in any ways
# print('a is outside the function',a)

#nested fucntions
# g=10
# def add():
#     return 0
# def outer_var():
#     outer_var='outer_var123'
#     print('global varibles insde outer function', globals())
#     print('local varibles insde outer function', locals())
#     def inner_var():
#         inner_var='inner_var123'
#         print('global varibles insde inner function', globals())
#         print('local varibles insde inner function', locals())
#         print('outer var inside inner function',outer_var)
#         print('e is',e)
#     e=40
#     print('global varibles insde outer function', globals())
#     print('local varibles insde outer function', locals())
#     inner_var()
# outer_var()


# if same varibale in global ,local and enclose space ---LEGB rule
a=10
def out():
    a=20
    def inn():
        global a #global will get updated to the new value
        a=30
        print('a value is',a)
    inn()
out()
print('a value is',a)
