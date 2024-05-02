d={}
print("methods present in dict",dir(d))
d[1]='Kesav'
d[2]='Ram'
print(d)
d.update({3:'Anand',4:'Chaintanya'}) #Update method to add elements to dict

print('Data after update',d)

d2={1:'Kesav',1:'Bala',1:'Chaitu'}

d2.update({2:('Kesav','Bala','Chaitu')})
print(d2)
# d2[2][1]='Raghav'# we can't override tuple values
print(d2[2][1])