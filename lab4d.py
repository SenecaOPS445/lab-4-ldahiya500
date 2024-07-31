#!/usr/bin/env python3
# Strings 1
#AuthorID = lakshay2@myseneca.ca
#Author = lakshay

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(s):
    # Returns the first five characters of the string
    return s[:5] 

def last_seven(s):
    # Returns the last seven characters of the string
    return s[-7:]

def middle_number(num):
    # Converts the number to a string and returns the second and third characters
    num_str = str(num) # here the argument is converted into a string
    if len(num_str) < 3: # middle case only possible if it has more than 3 characters or number
        return num_str[1:]  # Return from the second character to end
    return num_str[1:3] # return the middle character

def first_three_last_three(s1, s2):
    # Returns a string that starts with the first three characters of s1 and ends with the last three characters of s2
    return s1[:3] + s2[-3:] # gives out first 3 and  last 3 

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))