# def outer_fun(a, b):
#     def inner_fun(c, d):
#         return c + d
#     return inner_fun(a, b)
#
# res = outer_fun(5, 10)
# print(res)

# def display_person(**args):
#     for i in args:
#         print(i)
#
# display_person(name="Emma", sal="25")

# def display(**kwargs):
#     for i,j in kwargs.items():
#         print(i,j)
#
# display(emp="Kelly", salary=9000)
#
# def add():
#
#     return 100,500
#     return 400
#     return 600
#
# print(add())


# def fun1(num):
#     global num
#     num =num
#     print(num)
#     return num + 25
#
# fun1(5)
# print(num)

x = 0
while x < 10:
    x = x + 1
    print("x value inside while",x)

print(x)