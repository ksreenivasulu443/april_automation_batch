var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)

################################################
str1 = "PYnative"
print(str1[1:4], str1[:5], str1[4:], str1[0:-1], str1[:-1])
####################################################
str1 = 'Welcome'
print (str1[:6] + ' PYnative')

str = "my name is James bond";
print (str.capitalize())

st1 = "pynative"
st2 = "pynative"
print(st1 == st2)
print(st1 is st2)

str1 = "My salary is 7000";
str2 = "7000"

print(str1.isdigit())
print(str2.isdigit())

str = "My salary is 7000";
print(str.isalnum())


str1 = "my isname isisis jameis isis bond";
sub = "is";
print(str1.count(sub, 4))


aList = [5, 10, 15, 25]
print(aList[::-2])

sampleList = [10, 20, 30, 40, 50]
print(sampleList[-2])
print(sampleList[-4:-1])

resList = [x+y for x in ['Hello ', 'Good '] for y in ['Dear', 'Bye']]
print(resList)


aList = [4, 8, 12, 16]
aList[1:4] = [20, 24, 28]
print(aList)

sampleList = [10, 20, 30, 40, 50]
sampleList.pop()
print(sampleList)

sampleList.pop(2)
print(sampleList)

list1 = ['xyz', 'zara', 'PYnative']
print (max(list1))

sampleList = [10, 20, 30, 40]
del sampleList[0:6]#deleting all  all elements
print(sampleList)

l = [None] * 10
print(len(l))

aList = [10, 20, 30, 40, 50, 60, 70, 80]
print(aList[2:5])
print(aList[:4])
print(aList[3:])

my_list = ["Hello", "Python"]
print("-".join(my_list))

sampleList = [10, 20, 30, 40, 50]
sampleList.append(60)
print(sampleList)

sampleList.append(60)
print(sampleList)

aList = ["PYnative", [4, 8, 12, 16]]
print(aList[0][1])
print(aList[1][3])




