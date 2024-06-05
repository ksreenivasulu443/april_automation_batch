def ky(n):
    return [int(i) for i in n]

def vl(t):
    return sum(t[:3]) - t[3]

def inp(dictionary, key, value):
    dictionary[tuple(key)] = value

# Get input from the user
a = input("Enter values: ")
b = input("Enter values: ")

# Convert input strings to tuples of integers
res1 = ky(a)
res2 = ky(b)

# Calculate the results
vls1 = vl(res1)
vls2 = vl(res2)

# Store the results in a dictionary
dtc = {}
inp(dtc, res1, vls1)
inp(dtc, res2, vls2)

# Print the dictionary
print(dtc)