# write a code age using in put method print age >= 18 as eligible for
# < 18 print not eligible for vote

age = int(input("enter the number:"))
if age>=18:
    print("you are eligible for vote", age)
elif age+1==18:
    print("you are eligible for vote in next year", age)
elif age+2==18:
    print("you are eligible for vote in two year", age)
else:
    print("you are not eligible for vote", age)
# take marks using input method
# print if marks >= 70 as Grade A
# print if marks between 60 and 70 grade B
# print if marks between 50 and 60 grade c
# print if marks between 40 and 50 Grade D
marks = float(input("Scored marks: "))
if marks >= 70:
    print("Scored grade A")
elif 60 <= marks < 70:
     print("Scored grade B")
elif 50 <= marks < 60:
     print("Scored grade C")
elif 40 <= marks < 50:
    print("Scored grade D")
else:
    print("failed")



