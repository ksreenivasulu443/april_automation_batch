str = "This is Calgary"
#Reverse the string
str1= str[::-1]
print(str1)
print("#"*50)
#Convert the str into list
l=list(str)
print(l)
print("#"*50)

#Split the string
# this code is creted to reverse the string "This is Calgary" to "Calgary is this"
str = "This is Calgary"
str1 = (str.split()) # After spliting the str in gets converted to list
print(str1,"type of str",type(str1))
rev_str = str1.reverse()
print(rev_str)
print(str1)
print("#"*50)
#List
l = ['This','is','Calgary']
print(l)
rev_l = l.reverse()
print(rev_l)
print(l)

print("#"*50)
# Using for loop and str in Array
print(" this is original array")
str = ["This", "is", "Calgary"]
for x in str:
    print(x)
print("After array reverse")
str.reverse()
for x in str:
    print(x)


print("#"*50)
str = ["This", "is", "Calgary"]
#print(str[0])
n = (len(str))
for x in range(n, -1, -1):
   # print(x,end=" ")
    x1 = x-1
    if x1 >=0:
        print(str[x1])






