# find simple interest on Rs. 10,000 at the rate of 5% for 5 units of time.

p = 10000
t = 5
r = 5

sip_ints = (p * r * t)/100
print(sip_ints)

# find compound interest for given values.
# principal, rate, time
# ci = pri - pow((1+(rat/100)), tim) - pri
p1 = 10000
r1 = 10.25
t1 = 5

# print(pow(10, 2))

ci = p1 * pow((1+(r1/100)), t1)
ci_int = ci-p1
print(ci_int)

''' armstrong number
Input : 153
Output : Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153
'''
# inp = str(153)
# l = len(inp)
# print("length of l is", l)
# sum = 0
# for i in inp:
#     sum = pow(int(i), l)+ sum
#     print(sum)
# print(sum)

ip = str(153)
lts = []
sum = 0
l = len(ip)
for i in ip:
    a =f"{i}*{i}*{i}"
    lts.append(a)
    sum = sum + pow(int(i), l)
k = int(ip)
print(f"{lts[0]} + {lts[1]} + {lts[2]} =", sum)
if k == sum:
    print("The given number is armstrong number", sum)
else:
    print("The given number is not armstrong number", sum)


