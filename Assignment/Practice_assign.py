1.What are the built-in data types in Python?
ANS:The built-in data types in Python include12345:
Numeric types: int, float, complex
String: str
Sequence types: list, tuple, range
Binary types: bytes, bytearray, memoryview
Mapping: dict
Boolean: bool
Set: set, frozenset

2.Explain the difference between lists and tuples.
ANS:Lists are mutable, which means you can modify their elements after creation. You can add, remove, or change items in a list.
Tuples, on the other hand, are immutable. Once you create a tuple, you cannot modify its elements. They remain fixed throughout their lifetime1.

3.How do you differentiate between mutable and immutable data types in Python?
ANS:Mutable objects (e.g., lists, dictionaries) can be changed after creation.
Immutable objects (e.g., strings, integers, tuples) cannot be changed after creation

4.What is the purpose of dictionaries in Python?

5.How can you convert a string to a list in Python?
ANS:a.The split() method splits a string into a list of substrings based on a specified separator.
b.we can convert a string to a list of individual characters by slicing it.

6.What is the difference between remove() and pop() methods in Python lists?
ANS: Python Sets A set is a collection of unique data, meaning that elements within a set cannot
be duplicated. For instance, if we need to store information about student IDs,
a set is suitable since student IDs cannot have duplicates.

7.How can you check the data type of any object in Python?
count = 10
print("The value of count is", count)
print("Type of count is", type(count))
# <class 'int'>

count2 =[9, 8, 7]
print(type([9, 8, 7]))
# <class 'list'>
8.What are the different ways to create a copy of an existing list in Python?
ANS:
9.Explain the concept of slicing in Python lists and strings.
ANS:In Python, WE can slice a list to access a range of elements efficiently.
The slicing operator is the colon (:).
The syntax for list slicing is: Lst[Initial:End:IndexJump].

WE can obtain a sub-string from a given string by specifying the start and end indices.

10.How do you concatenate two lists in Python?
ANS:Using the + operator to combine the lists:
listone = [1, 2, 3]
listtwo = [4, 5, 6]
joinedlist = listone + listtwo
Output: joinedlist
[1, 2, 3, 4, 5, 6]

11.What is the difference between shallow copy and deep copy in Python?
ANS:
Shallow Copy:A shallow copy creates a new object that stores references to the original elements.
It only copies the top-level structure, not the nested objects.

Deep Copy:A deep copy creates a new compound object and then recursively inserts copies of the objects
found in the original.

12.How do you delete elements from a dictionary in Python?
ANS:The zip () function in Python is used to combine two or more iterable dictionaries into a single iterable, where corresponding elements from the input iterable are paired together as tuples. When using zip () with dictionaries,
it pairs the keys and values of the dictionaries based on their position in the dictionary.

13.What is the purpose of the sorted() function in Python, and how does it differ from the sort() method?

14.Explain the difference between local and global variables in Python.
ANS:Python Global variables are those which are not defined inside any function and have a
global scope
whereas Python local variables are those which are defined inside a function and their
scope is limited to that function only. In other words, we can say that local variables are accessible only inside the function in which it was initialized
whereas the global variables are accessible throughout the program and inside every function.

15.What are the characteristics of a Python tuple?
ANS:Ordered: Tuples maintain the order of their elements. The first item in a tuple has index 0, the second item has index 1, and so on1.
Unchangeable (Immutable): Once you create a tuple, you cannot modify its contents. You cannot add, remove, or change items after creation1. This immutability makes tuples useful for situations where you want to ensure data integrity.
Allow Duplicate Values: Tuples can store duplicate values. If you need to keep multiple occurrences of the same value, a tuple allows it1.
Can Contain Different Data Types: Tuple items can be of any data type—strings, integers, booleans, etc. You can mix different data types within a single tuple1.
Length Determination: To find out how many items a tuple contains, you can use the len() function1.
Creating a Tuple with One Item: If you want to create a tuple with only one item, remember to add a comma after the item. Otherwise, Python won’t recognize it as a tuple

16.How do you check if a key exists in a dictionary?
ANS: Using the in Operator: The simplest way to check if a key exists in a dictionary is by using the in operator. This operator evaluates the membership of a value. If the key exists, it returns True; otherwise, it returns False. Here’s an example:
Python

fruits_dict = {'apple': 5, 'banana': 3, 'orange': 2}
key = 'orange'
if key in fruits_dict:
    print('Key Found')
else:
    print('Key not found')

17.What is the purpose of the enumerate() function in Python?
ANS:The enumerate() function in Python is a built-in function that allows you to loop over an iterable object while also keeping track of the index of the current item. It returns an enumerate object, which contains pairs of index and value for each item in the iterable1.
This feature is particularly useful when you need not only the values from an iterable but also their indices