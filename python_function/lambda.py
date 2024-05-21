######################################################
#Lambda functions
# syntax:
# lambda par1,par2,par3...parn : expression
######################################################

def convert_cols_lower(col):
    return col.lower()

print(convert_cols_lower('firstName'))


convert_cols_lower = lambda col: col.lower().strip(' 123')
print(convert_cols_lower('FIRST_NAME'))
#
cols = ('Full_Name ', ' First_name ', 'last_Name123', 'middle_name', 'Suffix_name', 'Phone_1','Email_1')
print("before conversion", cols)

# map function syntax
# map(function_name, values)

after_conversion = map(convert_cols_lower, cols)
print(list(after_conversion))


cols = ('Full_Name', 'First_name', 'last_Name', 'middle_name', 'Suffix_name', 'Phone','Email')
#
select_name_columns = lambda col: col.upper().endswith('NAME')

# print(select_name_columns('firstname'))
#
print("all columsn", cols)
select_cols = tuple(filter(select_name_columns, cols))
print("after filter cols endwith name",select_cols)

after_conversion = tuple(map(convert_cols_lower, select_cols))
print("After select and convert to lower",after_conversion)

ls = [1,2,3,4,5]
print("sum of all values in ls", sum(ls))
#print("mul of all values in ls", mul(ls))


from functools import *

# ls = [10, 20, 30, 40, 50]
add_two_value = lambda a,b:a+b
print(add_two_value(4,5))

mul_two_value = lambda a,b:a*b
print(mul_two_value(4,5))
ls = [10, 20, 30, 40, 50]
print("sum of all values in ls", sum(ls))
print(reduce(add_two_value,ls))

print(reduce(mul_two_value,ls))

# map -- i/p = o/p - same number values
# filter - o/p <= i/p
# reduce - only one output


ls = [10, 20, 30, 40, 50]
def mul_list_value(ls):
    mul=1
    for i in ls:
        mul = mul *i
    return mul
print("mul value using for loop",mul_list_value(ls))




# result = reduce(lambda x, y: x + y, ls)
# print(result)  # 150
#
# print("l sum",sum(ls))

# cal = lambda a, b: a + b
# print(cal('4', '5'))
#
