 # print Pattern * in square 10 x 10

square_side = int(input("Please Enter any Side of a Square  : "))

print("Square * Pattern")

# iterating number of rows
for i in range(square_side):
    # iterating number of column
    for i in range(square_side):
        print('*', end=' ')
    print()


# print Pattern * in left side increasing triangle
tri_side = int(input("Please Enter the left side of a left side increasing triangle : "))

print("left Side increasing triangle * Pattern")

# iterating number of rows
for i in range(tri_side):
 # iterating number of column
    for i in range(i+1):
        print('*', end=' ')
    print()


# print Pattern * in left side decreasing triangle
tri1_side = int(input("Please Enter the left side of a left side decreasing triangle : "))
print("left side decreasing triangle * Pattern")

# iterating number of rows
for k in range(tri1_side):
    # iterating number of column
    for l in range(k, tri1_side):
        print('*', end=" ")
    print()


# print Pattern * in empty decreasing and increasing triangle from right hand side
rt_side = int(input("Please Enter the right of a right increasing triangle  : "))

print("right Side increasing triangle * Pattern")

# iterating number of rows
for k in range(rt_side):
    # iterating number of column
    for l in range(k, rt_side):
        print(' ', end=" ")

    for l in range(k+1):
        print('*', end=' ')
    print()

rtd_side = int(input("Please Enter the right Side of a right Side decreasing triangle  : "))

print("right Side decreasing triangle * Pattern")

# iterating number of rows
for k in range(rtd_side):
    # iterating number of column
    for l in range(k+1):
        print(' ', end=' ')

    for l in range(k, rtd_side):
        print('*', end=" ")
    print()

# print Pattern * in Hill
hill_side = int(input("Please Enter any Side of a pyramid  : "))

print("pyramid * Pattern")

# iterating number of rows
for k in range(hill_side):
    # iterating number of column
    for l in range(k, hill_side):
        print(' ', end=" ")

    for l in range(k):
        print('*', end=' ')

    for l in range(k+1):
        print('*', end=' ')
    print()


# print Pattern * in revers Hill
revers_hill = int(input("Please Enter any Side of a revers pyramid  : "))
print("revers pyramid * Pattern")

# iterating number of rows
for k in range(revers_hill):

    # iterating number of column
    for l in range(k+1):
        print(' ', end=' ')
    for l in range(k, revers_hill-1):
        print('*', end=" ")
    for l in range(k, revers_hill):
        print('*', end=" ")
    print()

# print Pattern * in dimond
revers_hill = int(input("Please Enter any Side of a dimond  : "))
print("dimond * Pattern")
 # iterating number of rows
for k in range(hill_side-1):
    # iterating number of column
    for l in range(k, hill_side):
        print(' ', end=" ")

    for l in range(k):
        print('*', end=' ')

    for l in range(k+1):
        print('*', end=' ')
    print()

# iterating number of rows
for k in range(revers_hill):

    # iterating number of column
    for l in range(k+1):
        print(' ', end=' ')
    for l in range(k, revers_hill-1):
        print('*', end=" ")
    for l in range(k, revers_hill):
        print('*', end=" ")
    print()