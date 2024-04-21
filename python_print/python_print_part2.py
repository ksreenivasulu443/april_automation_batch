""" This file is created to practice python print function using format string
    created by: Sreeni on 04/19/2024
"""

#Import section
import sys
import os
import datetime

#
name = 'Sreeni'
age = 20
print(f"name is {name} and age is {age} ")
print("name is", name, "and age is", age, sep='')
source_cnt = 10
target_cnt = 20
print("source count is", source_cnt, "target count is", target_cnt, "and difference is " ,source_cnt-target_cnt)
print(f"source count is {source_cnt} and target count is {target_cnt} and difference is {source_cnt-target_cnt}")

batch_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

file = open(r"C:\Users\A4952\PycharmProjects\Sreeni\text"+batch_id+".txt", 'a')
original = sys.stdout
sys.stdout = file

print(source_cnt, target_cnt, sep='-', end='\t', file=file )
print("Execution is completed!!!")
print("hello world")

print("hello world")

for i in range(1,10):
    print(i)