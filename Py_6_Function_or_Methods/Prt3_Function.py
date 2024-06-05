from sympy.printing.numpy import func


def fnd_chr(name, char):
    chr_cnt = name.count(char)
    print(chr_cnt)
    return name, char, "count is", chr_cnt


result = fnd_chr("ETL Testing Automation", "T")
# print(occ("ETL Testing Automation"))
print(result)


def char_cnt1(a, b, c):
    count = 0
    count1 = 0
    for i in a:
        if i == b:
            count = count + 1

        elif i == c:
            count1 = count1 + 1
        else:
            pass

    return a, b, "count is", count, "and", c, "count is", count1


print(char_cnt1("ETL Testing Automation", "t", "a"))


# find Maximum of three numbers
def max_num(a, b, c):
    tp =[]
    for i in a,b,c:
        tp.append(i)
        mx = max(tp)
        mn = min(tp)
    print("max value is", mx, "and min value is", mn)
    return mx, mn

print(max_num(1, 9, 5))


# List = [1,2,3,4,5]
# Max = 0
#
# for x in List:
#     if x > Max:
#         Max = x
#
# print(Max)

# Write python function to print factorial of numbers
def fac_num(a):
    fact =1
    for i in range(1, a + 1):
        fact = fact * i
    return fact

print(f"factorial of a is", fac_num(4))


def factorial11(n):
    if n == 0:
        return 1
    else:
        a =n * factorial11(n-1)


        return a

print("fct of 5 is", factorial11(5))

def factorial1(n):
    result = 1
    for i in range(1, n + 1):
        result *= i  # result = result * i
    print(f"factorial1 of {n} is", result)
    return result

factorial1(5)


# # Example usage:
# print(factorial(6))  # Output: 120
# factorial(6) calls factorial(5) * 6.
# factorial(5) calls factorial(4) * 5.
# factorial(4) calls factorial(3) * 4.
# factorial(3) calls factorial(2) * 3.
# factorial(2) calls factorial(1) * 2.
# factorial(1) calls factorial(0) * 1.
# factorial(0) returns 1 (base case).

# factorial(1) returns 1 * 1 = 1.
# factorial(2) returns 1 * 2 = 2.
# factorial(3) returns 2 * 3 = 6.
# factorial(4) returns 6 * 4 = 24.
# factorial(5) returns 24 * 5 = 120.
