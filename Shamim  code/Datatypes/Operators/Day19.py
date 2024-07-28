for i in range(1,4):
    for j in range (1,5):
       #print("i and j value is",i,j)
       print(f"{i} * {j} = {i,j}")
 #################################################333

n = int(input("enter number"))
for i in range (1,n+1):
    for j in range (1,n+1):
        # print(i,end=' ')  print(i,end='\t ')  print(i,end='\.n')
           print(i,j)
##########################################################
     #break statement:
data = [1,2,3,4,5,0,6,7,0,8]
for i in data:
    if i == 0:
         break
    print(10/i)
  ########################################################
    #Continue:

num=10
for i in data:
        if i == 0:
            continue
        print(f"i value is {i},{num}/{i}",num/i)

##################################################
#Pass: it will eexecite the code any condition declaired.

for i in range(1,10):
    pass
