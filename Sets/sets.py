s={1,4,3,4,5,6}
d={1:'ram',2:'sree'}

print('fetch set',s)
print('fetch d',d)
print('fetch set',type(s))
print('fetch d',type(d))
d2={}
print('fetch d',type(d2))
s2=set()
print('fetch set',type(s2))
print('fetch d2',d2)
print('fetch s2',s2)
#print(s2[0]) 'set' object is not subscriptable
l1=list(s) # converting set to list
print(l1[0])

print('methods in set',dir(s))
# adding element to the set
s.add(10)
print('fetch set',s)
# updating set
s.update({11,11,12,13})
print('fetch set',s)
s.update(('sree'))
print('fetch set',s)
s.add('raam')
print('fetch set',s)
s.update('sree','100')
print('fetch set',s)
#s.update('sree',200) #int' object is not iterable
#print('fetch set',s)
#delete element from set --pop will delete last/random element from the set
#s.pop()
popped_element=s.pop()
print('remove element',popped_element)
# remove -we can remove specified element
#s.remove('raam')
#print('after remove the set is ',s)
#s.remove(201) --if there is no value in the set that we try to remove it will throw key error
print('after remove the set is ',s)
#discord - we can avoid the runtime error for trying to delete the value which is not in set
s.discord(201)
print('after discord the set is ',s)