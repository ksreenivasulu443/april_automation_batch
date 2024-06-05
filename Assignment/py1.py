# Python | Sort Python Dictionaries by Key or Value


myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}

lt = []
for i in myDict.items():
    lt.append(i)
lt.sort()
dic = dict(lt)
print(dic)


myDict1 = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
def srt_dic(a):
    ls = list(a.items())
    ls.sort()
    dct = dict(ls)
    print(dct)

srt_dic(myDict1)


def dictionary():
    # Declare hash function

    key_value = {}
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323
    print(key_value)
    for i in sorted(key_value.keys()):
        print(i, end=" ")
    print()

dictionary()


# Handling missing keys in Python dictionaries

try:
    d = { 'a' : 1 , 'b' : 2 }
    print(d['c'])

except KeyError as e:
    print("KeyError pass valid key, please retry:", e)


# Python dictionary with keys having multiple inputs


# b = input("enter values")
# c = input("enter values")



# ts = []
# for i in res:
#     ts.append(i)
# gs = ts[0] + ts[1] + ts[2] - ts[3]
# print(gs)

# ac = tu[0]+tu[1]-tu[3]
# ad = c[0]+c[1]
# dc = {a:ab, b:ac, c:ad}
a = input("enter values")
b = input("enter values")
def ky(n):
    tu = []
    for i in n:
        tu.append(int(i))
    return tu

res1 = tuple(ky(a))
res2 = tuple(ky(b))


def vl(b):
    ts = []
    for i in b:
        ts.append(i)
    gs = ts[0] + ts[1] + ts[2] - ts[3]
    return gs

vls1 = vl(res1)
vls2 = vl(res2)

dtc = {}
def inp(dictionary, key, value):
    dictionary[key] = value


inp(dtc, res1, vls1)
inp(dtc, res2, vls2)
print(dtc)

