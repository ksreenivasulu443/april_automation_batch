# write a code display even and odd number from the list
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_ls = []
odd_ls = []
for i in ls:
    if i%2 ==0:
        print(i, end='\n')
        even_ls.append(i)
    elif i%2 !=0:
        odd_ls.append(i)

print(even_ls)
print(odd_ls)

# write a code display even and odd number from the tuple.
# Tuple is immutable.
tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
lstp = []
lstp1 = []
for i in tp:
    if i%2 == 0:
        # print(i, end='\n')
        lstp.append(i)
    elif i%2 != 0:
        lstp1.append(i)

even_tp = tuple(lstp)
odd_tp = tuple(lstp1)

print("even number in tuple is", even_tp)
print("odd number in tuple is", odd_tp)


