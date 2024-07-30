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




