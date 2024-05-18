'''
There are 4 types are actual arguments are allowed in Python.
1. positional arguments : These are the arguments passed to function in correct positional order.
2. keyword arguments: We can pass argument values by keyword i.e by parameter name.
3. default arguments : Sometimes we can provide default values for our positional arguments.
4. Variable length arguments : Sometimes we can pass variable number of arguments to our function,such
type of arguments are called variable length arguments.

Note: While calling function if passing positional argument and keyword argument -- should follow
 always positional argument should pass 1st then should pass keyword argument
'''

# 1. positional arguments
def cal(a, b, c):
    sum = a+b+c
    print("sum of a,b,c is", sum)
    return sum


cal(100,200, 200)  # while calling function should pass only value in order. -positional arguments

# 2. keyword arguments
cal(b=30, a=20, c=20)  # while calling function should pass with key and value. -keyword arguments

#3. default arguments  # while creating in function should pass the key and value like (d=nth value)

def cal1(a, b, c, d=0):
    sum = a+b+c+d
    print("sum of a,b,c and d default value is", sum)
    return sum

cal1(10,20, 20)

cal1(10, 20, 20, 10)  # d=0 overwritten with d =10

cal1(10, 20, c=20, d=10)

# int to string convert and adding

def student(name, m1, m2, m3, m4, m5=0):
    tot_mrk = m1+m2+m3+m4+m5
    print(f"Student Name is {name} and total marks in midterm is {tot_mrk}")
    st_mrk = str(tot_mrk)
    return name+st_mrk


print(student("Arjun", 50, 75, 49, 90))


# when need pass many arguments
def calc(*args):
    print(args)
    sum=0
    for i in args:
        sum = i + sum
    return sum

print("sum of args is", calc(1, 2, 3))
print("sum of args is", calc(1, 2, 3, 4))
print("sum of args is", calc(1, 2, 3, 4, 5))


# a = [1, 4, 6]
# b = [2, 4, 8]
def calc1(a, b):
    print("list values", a)
    print("list values", b)
    ls = a+b
    print("list values", ls)
    sum=0
    for i in ls:
        sum = i + sum
    return sum

print("sum of list values is", calc1([1, 4, 6], [2, 4, 8]))


def fruits(ls1):
    i = 0
    while i <= len(ls1):
        if ls1[i] == "Coconut":
            print(ls1[i])
            break
            # print(ls1[i])
        i = i + 1
    return ls1[i]

print("Search completed and fruit is", fruits(ls1 = ["Apple", "Banana", "Coconut"]))


num = input("Enter the numbers:")  # 2, 4, 6, 8 in text format
numbers = num.split(",")
res = [eval(i) for i in numbers]
print("Modified list is: ", res)



l = ['1', '2', '3', '4']

for i, item in enumerate(l):

    try:
        l[i] = int(float(item))
    except ValueError:
        l[i] = item

print(l)
# ld = eval(l)
# print(ld)

lis = ['1', '-4', '3', '-6', '7']
res = [eval(i) for i in lis]
print("Modified list is: ", res)

lis1 =[]
for i in lis:
    res = eval(i)
    lis1.append(res)

print(lis1)



