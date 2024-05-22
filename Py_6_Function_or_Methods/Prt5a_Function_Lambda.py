cols= ['Full_Name','First_name','last_name','middle_name', 'Suffix_name','Phone']

# method 1 convert to Single value in lower in Lambda
convert_cols_lower = lambda col : col.lower()
print(convert_cols_lower('Sreeni'))

# method 2 Find fullname end with name from List value convert lower in Lambda and Filter
select_name_columns = lambda col : col.lower().endswith('name')
sel = filter(select_name_columns, cols)
print(list(sel))


# method 3 convert to List value in lower in Lambda and Map
cols1= ['Full_Name','First_name','last_name','middle_name', 'Suffix_name','Phone']
convert_cols_lower1 = lambda col : col.lower()
after_conversion = map(convert_cols_lower1, cols1)
print(list(after_conversion))

