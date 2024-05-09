d={}
print('method',type(d))
#print('methods available in dictioanry',dir(d))

d[1]='sreeni'
d[2]='deepu'
print(d)
d.update({3:'RAM'})
print('after updating the dictionary',d)

d2={1:'River',2:'john',3:'wolf'}
#variable={key1:value,key2:vale2,key3:value3}
print(d2)
d2.update({1:'rowdy',4:'Sree'})
print('after update d2',d2)
d2.update({1:'rowdy',4:['Sree','deepu']})
print('after update d2',d2)
d2.update({1:'rowdy',5:('Sree','deepu')})
print('after update d2',d2)
d2.update({1:'rowdy',5:('Sre','deepu')})
print('after update d2',d2)

d2[7]=10.2
d2[8]=1+3j
print('after update d2',d2)


