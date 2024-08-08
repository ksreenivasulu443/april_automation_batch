str = [1, 'nivi', '@']

ls = [1, 2.0, True, 1 + 2j, 'string']

# print("the values of list is : ",ls)
# print("type of list is :",type(ls))
# print("memory address of the list :",id(ls))

# print("the first_element in the list is :",ls[0])
# print("the second_element in the list is :",ls[1])
# print("the third_element in the list is :",ls[2])
# print("the fourth_element in the list is :",ls[3])
# print("the five_element in the list is :",ls[4])

# print("the first_element in the list is :",ls[0],type(ls[0]))
# print("the second_element in the list is :",ls[1],type(ls[1]))
# print("the third_element in the list is :",ls[2],type(ls[2]))
# print("the fourth_element in the list is :",ls[3],type(ls[3]))
# print("the five_element in the list is :",ls[4],type(ls[4]))

# print("the first_element in the list is :", ls[0], type(ls[0]), id(ls[0]))
# print("the second_element in the list is :", ls[1], type(ls[1]), id(ls[1]))
# print("the third_element in the list is :", ls[2], type(ls[2]), id(ls[2]))
# print("the fourth_element in the list is :", ls[3], type(ls[3]), id(ls[3]))
# print("the five_element in the list is :", ls[4], type(ls[4]), id(ls[4]))

print("*" * 50)

ls0 = [1, 2.0, True, 1 + 2j, 'string']
print("slice the ls0 value ls[0:2] is :", ls0[0:2])
print("slice the ls0 value ls[0:2] is :", ls0[0:5])
print("slice the ls0 value ls[0:2] is :", ls0[0:5:2])
print("slice the ls0 value ls[0:2] is :", ls0[0:2:-1])

ls1 = []
print("print the empty list1 :", ls1)

ls2 = list()
print("print the empty list2 :", ls2)

print("the value of the list is:", ls2)
print("the type of the list2 is :", type(ls2))
print("the memory address of the list2 is :", id(ls2))

print("the methods available in the list is :", dir(ls2))
"""'append', 'clear', 'copy', 'count', 'extend', 'index',
   'insert', 'pop', 'remove', 'reverse', 'sort'"""

print("before append the list2 value is :", ls2)
(ls2.append(5), ls2.append('@'), ls2.append('nivi'), ls2.append(2 + 2j))
print("after append the list2 value is :", ls2)
print("after append the list2 value is :", ls2, type(ls2))
print("after append the list2 value is :", ls2, id(ls2))

ls2.insert(5, 984598), ls2.insert(3, 'Prashant'), ls2.insert(-1, '@@'),
print("after insert the values in list2 value is :", ls2)

ls2.append([1, 2])
print("after append the list2 value is :", ls2)

ls2.extend([1, 2, 8, 70167])
print("after append the list2 value is :", ls2)

ls2.extend('iiiiii')
print("after append the list2 value is :", ls2)

a = ls2.count('i')
print("after append the list2 value is :", a)
print("count of the i in ls2is : ", ls2.count('i'))

ls3 = ls2.copy()
print("ls3 is the copy ls2 :", ls3)
print("the values of ls3 is :", ls3)

ls2.pop()
ls2.pop(0)
ls2.pop(3)
print("after the pop of ls2 is :", ls2)
print(ls2)
print(ls3)

print("*" * 120)

# print(ls2)
# print(ls3)

print("before removing values in ls2 is :", ls2)
ls2.remove('@')
print("after removing values in ls2 is :", ls2)

print("before removing values in ls2 is :", ls2)
ls2.remove([1, 2])
print("after removing values in ls2 is :", ls2)

print("-" * 110)

# print(ls2)
ls2.index(2)
print(ls2)

print("-" * 110)

ls5 = [1, 'Nivi', True, 10.5]
print("ls5':", ls5)

ls5.reverse()
print("ls5':", ls5)

print("ls5[2][::-1] is :", ls5[2][::-1])

print("-" * 100)

ls6 = ['Prashant', 'Nivi', 21, 15.5]
print("before reverse the ls6:", ls6)
ls6.reverse()
print("after reverse the ls6:", ls6)
print("ls6[3][::-1] : ", ls6[3][::-1])

ls_1 = [1, 2, 3]
ls_2 = [3, 4, 5]
print("list addition ls, ls_1", ls_1 + ls_2)
print("list multiplication ls_2", ls_1 * 2)

f_name = 'Prashant'
l_name = 'Nivi'
print("f_name + l_name :", f_name + l_name)
# print("f_name * l_name :",f_name * l_name)
print("f_name + l_name :", f_name * 2)

a = 10
b = 20
print("a + b :", a + b)
print("a * b :", a * b)

t = (1, 2, 3)
ls_1 = [1, 2, 3]
print("before convert", type(ls_1))
print("before convert", type(t))
ls_1 = tuple(ls_1)
print("after convert to tuple", type(ls_1))
t = list(t)
print("after convert to list", type(t))
