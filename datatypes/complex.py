"""This module file is create to practice python complex datatypes
   created by Prashant on 04/23/2024"""


# 2 real, 1 imagi, j = sqrt(-1))
c = 2.0 + 1j
print("The value of c is", c)
print("Type of c is", type(c))
print("Memory address of c is", id(c))
d = 1j
print("The value of d is", d)
print("Type of d is", type(d))
print("Memory address of d is", id(d))
e = 0.1 + 1j
print("The value of e is", e)
print("Type of e is", type(e))
print("Memory address of e is", id(e))
print("methods available:", dir(e))
print(f"Imaginary value {e}", e.imag)
print(f"real value{e}", e.real)

