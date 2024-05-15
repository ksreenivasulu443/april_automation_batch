# for i in range(1,11):
#     #print("i value is",i)
#     for j in range(1,11):
#         #print("i and j value are",i,j)
#         print(f" {i} * {j} = {i * j}")

#
# for i in range(1,6):
#     print("#" *i)

#
# n = int(input("enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         #print("i and j values ",n)
#         print(i,end=' ')
#     print()
#
# n = int(input("enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         #print("i and j values ",n)
#         print(j,end=' ')
#     print()


# Function to sum numbers using a for loop def sum_with_for_loop(n):
total = 0
for i in range(n):

      total += i

      return total

# Function to sum numbers using a while loop def sum_with_while_loop(n):
    total = 0
    i = 0
    while i < n:
        total += i
        i += 1
    return total

# Measure execution time for the for loop
print("Time taken by for loop:", timeit.timeit(lambda: sum_with_for_loop(1000000), number=1))

# Measure execution time for the while loop
print("Time taken by while loop:", timeit.timeit(lambda: sum_with_while_loop(1000000), number=1))
