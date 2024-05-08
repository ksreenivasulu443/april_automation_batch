"""
Conditional Statements :
need use Comparison Operators (>,>=,<,<=, ==, !=)

if :  condition is true then If Block statements will be executed.
if-elif : When If Block false then elif block will be executed.
if-elif-else : When If and elif Block false then Else block will be executed.
if-else : if condition is False then if block will not execute and Else block will be executed.

"""

Name = input("Enter Name:")
# Methods "If"
print("------'Methods 'if' block execution'------")
if Name == "Ram":
    print("Inside if block executed")
    print(f"Hello {Name}, Good Morning")

# Methods "if-elif"
print("------'Methods 'if-elif' block execution'------")
Name1 = input("Enter Name:")
if Name1 == "Ram":
    print("Inside if block executed")
    print(f"Hello {Name1}, Good Morning")
elif Name1 == "Raju":
    print("Inside elif block executed, Name1 == 'Raju'")
    print(f"Hello {Name1}, Good Morning")
elif Name1 == "Soma":
    print("Inside elif block executed, Name1 == 'Soma'")
    print(f"Hello {Name1}, Good Morning")

# Methods "if-elif-else"
print("------'Methods 'if-elif-else' block execution'------")
Name2 = input("Enter Name:")
if Name2 == "Ram":
    print("Inside if block executed")
    print(f"Hello {Name2}, Good Morning")
elif Name2 == "Raju":
    print("Inside elif block executed, Name1 == 'Raju'")
    print(f"Hello {Name2}, Good Morning")
else:
    print(f"Name2 =={Name2} not present in if & elif block, else block executed")
    print(f"Hello {Name2}, Good Morning")

# Count Comparison
source_cnt = int(input("Enter the source record count:"))
target_cnt = int(input("Enter the target record count:"))

if source_cnt == target_cnt == 10:
    print("source_cnt & target_cnt is equal to 10")
elif source_cnt == target_cnt == 79:
    print("source_cnt & target_cnt is equal to 79")
else:
    print(f"source_cnt {source_cnt} & target_cnt {target_cnt} is not equal to if & elif block Condition count")
