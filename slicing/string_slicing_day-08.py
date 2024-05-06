"""This module file is create to practice python slicing and
   created by Prashant on 30/04/2024"""

# start position

str = 'ETL'
print("str")
print("str value is : ", str)

# start position
print("#End position")
print("-"*75)
print(f"first character available in {str} is : ", str[0])
print(f"second character available in {str} is : ", str[1])
print(f"third character available in {str} is : ", str[2])
print(f"first character available in {str} is : ", str[0])

print(f"in {str},first character available is {str[0]},"
      f"second character available is {str[1]},"
      f"third character available is {str[2]}")

for i in str:
    print("value available is",i)

# End position
print("#start position")
print("-"*100)
str = 'ETL AUTOMTION'
print(f"the character available in {str} : ",str)
print(f"0:6 character available in {str} :",str[0:6])# end = end-1 , str [0 to 5 character]
print(f"0:4 character available in {str} :",str[0:4])# end = end-1 , str [0 to 3 character]
print(f"0:2 character available in {str} :",str[0:2])# end = end-1 , str [0 to 1 character]
print(f"0: character available in {str} :",str[0:])
print(f"5: character available in {str} ",str[5:])
print(f"[:]the character available in {str} are :",str[:])
print(f"[4:6] the character available in {str} is : " ,str[4:6])


email = 'etldev2023@gmai.com'
print(f"user_name from {email} is : ",email[0:email.find('@')])
print(f"user_name from {email} is : ",email[email.find('@'):])
print(f"user_name from {email} is : ",email[email.find('@')+1:])

str = 'ETL AUTOMATION'
print(f"str.find('A') is : " ,str.find('A'))
print("str.rfind('A') is : " ,str.rfind('A'))


# step position
print("#step position")
print("="*100)

str = 'Prashant Belagavi'
print("[0:12:1] the available character in {str} are :",str[0:12:1])
print(f"[0:8] the available character in {str} are :",str[0:8])
print(f"[9:18]the last_name character available in {str} is :",str[9:18])
print(f"[0:8] the last_name character available in {str} is :",str[0:8])
print(f"fetch the character from the {str} :",str[0:9:1])
print(f"the character available in the {str} is :", str[2:6:2])
print(f"the character are in the {str} are :",str[0:17:1])  
print(f"the thd available character in {str} is :", str[5:13:3])