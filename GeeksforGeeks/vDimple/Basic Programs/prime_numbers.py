# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 22:00:42 2021

@author: dimpl
"""

# Python program to print all Prime numbers in an Interval

# range_start = int(input("Enter starting of range: "))
# range_end = int(input("Enter end of range: "))
# for number in range(range_start, range_end):
#     flag = False
#     for each in range(2, number+1//2):
#         if number % each == 0:
#             flag = True
#             break
#     if flag == False:
#         print(number)


# Python program to check whether a number is Prime or not
while True:

    number = int(input("Number: "))
    # if number == 1 or number == 2:
    #     print("prime")
    flag = False
    for each in range(2, number+1//2):
        if number % each == 0:
            flag = True
            print("Not prime")
            break
    if flag == False:
        print("prime")
