
# syntax:
# lambda par1,par2,par3...parn : expression

cal = lambda a,b:a+b

print(cal('4','5'))

# def convert_cols(col):
#     return col.lower()

convert_cols_lower = lambda col : col.lower()

print(convert_cols_lower('Sreeni'))

cols= ['Full_Name','First_name','last_name','middle_name', 'Suffix_name','Phone']
print("before conversion", cols)

# map function syntax
# map(function_name, values)

after_conversion = map(convert_cols_lower,cols)

print(list(after_conversion))
#
cols= ['Full_Name','First_name','last_name','middle_name', 'Suffix_name','Phone']

select_name_columns = lambda col : col.lower().endswith('name')

sel = filter(select_name_columns, cols)

print(list(sel))
