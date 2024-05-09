"""f --it executes the statements when conditiion is tru"""
#syntax for if statement
#if condition:
#    code
#name= input('enter name')
#if name=='Sreeni':
#print('inside the if statement')
#print(f'hello {name},good moring') # indentation should be uniform across the code



#################################################################
# syntax for if-elif
#name= input('enter name')
#name='Sreeni'
#if name=='Sreeni':
# print('inside the if statement')
# print(f'hello {name},good moring')
#elif name=='Raj':
# print('inside the elif statement')
# print(f'hello {name},good moring')
#elif 10:
# print('inside the elif statement')
# print(f'hello {name},good moring')
#print('this print is outside the if')
#########################################
#if-elif-else
#if condition:
#   code
#elif condition:
#   code
#else:
#    code


#name='Sreeni'
#name= input('enter name')
#if name=='Sreeni':
# print('inside the if statement')
# print(f'hello {name},good morning')
#elif name=='Raj':
# print('inside the elif statement')
# print(f'hello {name},good morning')
#elif name=='ram':
# print('inside the elif statement')
# print(f'hello {name},good morning')
#else:
# print('inside  of else')
# print('hello guest ,good morning')

# print numerics to words
#number=int(input('enter number'))
#if number==0:
 #print(f'entered number is ZERO')
#elif number==1:
 #print(f'entered number is ONE')
#elif number==2:
 #print(f'entered number is TWO')
#elif number==3:
 #print(f'entered number is THREE')
#elif number==4:
 #print(f'entered number is FOUR')
#elif number==5:
 #print(f'entered number is FIVE')
#else:
 #print('entered number is is not in between 0 to 5 please retry ')


# print + and negative values
#number=int(input('enter number'))
#if number>0 :
# print(f'{number} is positive ',number)
# elif number<0:
# print(f'{number} is negaitive ',number)
# else:
# print( number)

#number=float(input('enter number'))
#if number>0 :
# print(f'{number} is positive ',number)
#elif number<0:
# print(f'{number} is negaitive ',number)
#else:
# print(number)

# take age  and print if age>=18 eligible else if <18 not eligible for vote  and eligible for x years
#age=float(input('enter number'))
#if age>=18 :
 #print(f'eligible for vote {age}')
#else:
# print(f'not eligible for vote and you are eligible for vote aafter 18+{age}')

#take marks as input and print Grade A if marks>75 and
# marks between 70 -60'B"
#marks between 60-50 'C"
#marks between 50-40 'D"
#Marks less than 40 fail

#marks=float(input('enter marks'))
#if marks >=75:
# print(f'Grade-A and {marks}')
#elif marks>=60 and marks<=70:
 #print(f'Grade-B and {marks}')
#elif marks>=50 and marks<=60:
# print(f'Grade-C and {marks}')
#elif marks>=40 and marks<=50:
# print(f'Grade-D and {marks}')
#else:
# print(f'FAIL and {marks}')
#polyndrome
#str='madam'
#rev_str=str[::-1]
#if str==rev_str:
# print(f'{str} is a polyndrome')
#else:
# print(f'{str} is not a polyndrome')

#num=121
#num=str(num)
#rev_num=num[::-1]
#if num==rev_num:
# print(f'{num} is a polyndrome')
#else:
# print(f'{num} is not a polyndrome')

#abs function will return the postive even if it is negative
source_count=10
target_count=11
if source_count==target_count:
 print('count is  matching' )
else:
 print('count is not  matching and difference is ', abs(source_count - target_count))