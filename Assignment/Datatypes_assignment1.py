Python fundamental data types:

1. *Integer:*
A. What is the maximum and minimum value that can be represented by an integer in Python?
ANS:In Python 3, the int type corresponds to long in Python 2, and it has no maximum or minimum limit.
The concept of a maximum or minimum int disappears completely

B.Explain the difference between int() and float() conversion functions in Python.
ANS:The int() function is used to convert any data type to an integer.
num_str = "42"
num_int = int(num_str)  # Converts the string "42" to an integer 42
The float() function converts any data type to a floating-point number (i.e., a decimal number).
num_int = 100
num_float = float(num_int)  # Converts the integer 100 to a float 100.0

C.How do you convert a string containing a numerical value to an integer?
ANS:To convert a string containing a numerical value to an integer in Python,
We can use the built-in int() function.

D.Can you explain the concept of integer division and how it differs from regular division?
ANS: In Python, the division operator / performs regular division,
while // performs integer division (floor division).
In Python 3.x:
5 / 2 will return 2.5.
5 // 2 will return 2.

E.How would you check if a given number is even or odd in Python?

2. *Float:*
   - What is the difference between float and integer division in Python?
   - How do you ensure precision when dealing with floating-point numbers in Python?
   - Explain the significance of scientific notation in representing floating-point numbers.
   - How would you compare two floating-point numbers for equality in Python?
   - What are the potential issues with comparing floating-point numbers for equality?

3. *Boolean:*
   - What are the possible boolean values in Python?
   - How does Python interpret non-boolean values in a boolean context?
   - Explain the difference between the and, or, and not logical operators in Python.
   - How would you convert a non-boolean value to a boolean value in Python?
   - Describe a scenario where short-circuit evaluation of boolean expressions is beneficial.

4. *String:*
   - What are escape sequences in Python strings? Provide some examples.
   - How do you concatenate strings in Python?
   - Explain the difference between single quotes (''), double quotes ("") and triple quotes (''' ''') in Python.
   - How would you find the length of a string in Python?
   - What are some common string methods in Python, and how would you use them?

These questions cover a range of topics related to Python's fundamental data t