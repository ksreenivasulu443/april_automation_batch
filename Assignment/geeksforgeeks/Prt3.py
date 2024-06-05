# Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n.
# For example factorial of 6 is 6*5*4*3*2*1 which is 720.


fact = 1  # each iteration i value will change
for i in range(1, 6+1):  # n-1 = 6 -- 6*5*4*3*2*1
    fact = fact * i       # 1*1, 1*2, 2*3, 6*4, 24*5, 120*6 = 720
print(f"factorial of {4}", fact)


ls = [1, 2, 3, 4, 5, 6]
ft = 1
for i in ls:
    ft = ft * i

print("list Factorial", ft)



ls1 = [1, 2, 3, 4, 5, 6]
i = 0
sm = 1
while i < len(ls1):
    sm = sm * ls1[i]
    i = i + 1
print("while loop - 1 list Factorial", sm)


i1 = 6
sm1 = 1
while i1 >= 1:
    sm1 = sm1 * i1
    i1 = i1 - 1

print("while loop - 2 integer Factorial", sm1)


def fctl(a):
    su = 1
    for i in a:
        su = su*i

    return su


print(fctl([1, 2,3, 4,5,6]))



def factorial11(n):
    if n == 0:
        return 1
    else:
        a =n * factorial11(n-1)
        print(a, end=',')

        return a

print("fct of 5 is", factorial11(6))