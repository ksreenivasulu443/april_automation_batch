'''
while loop:
If we want to execute a group of statements iteratively until some condition false,then we
should go for while loop.

while condition :
 body
'''
print("increasing while loop")
i = 0
while i<=10: # infinite loop
    print(i)
    i = i+1  # range control

print("decreasing while loop")
i = 10
while i>=0: # infinite loop
    print(i)
    i = i-1  # range control

# list iteration
print("----------list iteration----------")
ls = [10, 20, 30, 40, 50]
i=0
while i < len(ls):
    print(ls[i])
    i +=1

ls1 = ["Apple", "Banana", "Coconut"]
i = 0
while i <= len(ls1):
    if ls1[i] == "Banana":
        print(ls1[i])
        break
        # print(ls1[i])
    i=i+1