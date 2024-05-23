# cal = lambda a,b:a+b
#
# print(cal('4','5'))

# convert_col_lower=lambda col:col.lower().endswith('name')
# col=['Fullname','Last_Name','MEHBOOB','EMAIL','middle_name',"first_NAME"]
# print("before conversion",col)
# after_conversion=map(convert_col_lower,col)
# print(list(after_conversion))

# #convert_col_lower=lambda col:col.lower().endswith('name')
# cols=['Fullname','Last_Name','MEHBOOB','EMAIL','middle_name','first_NAME','phone']
# #print("before conversion",cols)
# select_col_name=lambda col:col.lower().endwith('NAME')
# select_cols=lis(filter(select_col_name,cols))
# after_conversion=list(map(convert_col_lower))


# from functools import *
#
# mul_two_values=lambda a,b:a*b
# print(mul_two_values(4,5))
# ls=[10,20,30,40]
# print(reduce(mul_two_values,ls))

def display(**kwargs):
    for i in kwargs:
        print(i)

display(emp="Kelly", salary=9000)