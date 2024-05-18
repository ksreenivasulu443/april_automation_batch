from sympy.printing.numpy import func


def fnd_chr(name, char):
    chr_cnt = name.count(char)
    print(chr_cnt)
    return name, char, chr_cnt


result = fnd_chr("ETL Testing Automation", "T")
# print(occ("ETL Testing Automation"))
print(result)


def char_cnt1(a, b, c):
    count = 0
    for i in a:
        if i == b:
            count = count + 1
        else:
            if i== c:
                count = count + 1


    print(count)
    return count


print(char_cnt1("ETL Testing Automation", "t", "a"))


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