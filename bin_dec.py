# -*- coding: utf-8 -*-
"""
Created on Wed May 11 13:55:35 2022

@author: Ashin Alex
"""


import math

def one(power):
    value = 1 * pow(2,power)
    
    return(value)

def zero():
    return (0)

def decimal(string):
    sum_of_values = sum(string)
    
    return(sum_of_values)
    
def is_binary(num):
    for i in str(num):
        if i in ('0','1'):
            return True
        else:
            return False
     
def main():
    workon = False
    while workon == False:
        binary = input("Enter the Binary Number: ")
        workon = is_binary(binary)

        return binary
    else:
        workon = False
        



    
    

binary = main()
binary_str = str(binary)

#print(binary_str)
#print(type(binary_str))
decimal_addition = []
len_of_binary = len(binary_str)
#print(len_of_binary)
power = len_of_binary - 1

for digit in binary_str:
    if digit == '1':
        product = one(power)
        decimal_addition.append(product)
        power = power - 1
        
    else:
        power = power - 1
        pass
    
final_decimal = decimal(decimal_addition)

print(f"The Decimal = {final_decimal}")
     








