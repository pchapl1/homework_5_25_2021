# Code from lessons as python files

# In Class Exercises / HW
# Compound Interest
# Write a function that computes the compound interest of an intial investment, using principle rate and time

# Formula for compound interest: A = P(1 + R/100) t

# Where, A is amount P is principle amount R is the rate and T is the time span.

# Part 2: Convert function to a method of a class i.e. (class Finances, calc_compound_interest)


class Finances:

    def __init__( self, prin, rate, time ):
    
        self.principle = prin
        self.rate = rate
        self.time = time


    def calc_compound_interest(self):
        amount = self.principle*(1 + (self.rate/100)) * self.time
        return amount

    
a1 = Finances(100, .10, 50)
# a1.calc_compound_interest()



# ASCII Calculator
# ASCII (American Standard Code for Information Interchange), is a character encoding standard for electronic communication. ASCII codes represent text in computers, telecommunications equipment, and other devices.

# There is a function for finding the ascii value of a character here: https://docs.python.org/3/library/functions.html

# Write a function that asks the user for input, and then computes the sum of all the ascii values of the characters.

# "hello" -> 104 + 101 + 108 + 108 + 111 = 532
# Part 2: Given a list of words (from user input) determine which word has the highest ascii value.

def sum_ascii_val(word):
    total = 0
    for letter in word:
        ascii_val = ord(letter)
        total += ascii_val
    return total
sum_ascii_val('hello')

def max_ascii_val(seq):
    max_val = 0
    for item in seq:
        if sum_ascii_val(item) > max_val:
            max_val = sum_ascii_val(item)
    return f'{item} has the highest mav_val of {max_val}'
max_ascii_val(['hello', 'hi', 'helllllo'])



# Ambiguous Dates
# Dates can be written differently depending where you are in the world 05.05.2021 (the fifth of may 2021) 03.05.2021 (the third of may 2021 -> Europe, the 5th of march 2021 -> US) 05.03.2021 (the fifth of march 2021 -> Europe, the 3th of may 2021 -> US)

# Sample Inputs:

# 05.05.2021 -> non-ambiguous
# 03.05.2021 -> ambiguous
# 05.03.2021 -> ambiguous
# Write a function that detects if a date, written in the format NN.NN.NNNN where n is a digit [0-9] is ambiguous
# save all the dates of the year that are ambiguous and print to user
# Extra: write a function that converts the format NN.NN.NNNN to a date such as "the 5th of May, 2021" (HINT: Use string formatting, and lists of strings)

def ambiguous(text):
    x = text.split('.')
    if int(x[0]) == int(x[1]) or int(x[0]) > 12 or int(x[1]) > 12:
        return f'non ambiguous'
    return f'ambigous date'
# ambiguous('05.04.2021')


dates_list = []
for x in range(1,32):
    str_x = str(x)
    if len(str_x) < 2:
        str_x = '0' + str_x

    for y in range(1,32):
        str_y = str(y)
        if len(str_y) < 2:
            str_y = '0' + str_y
        val = str_x +  '.' + str_y +'.2021'
        if x == y or x > 12 or y > 12:
            pass
        else:
            dates_list.append(val)
        
# print(dates_list)




# Double Letters
# Analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

# Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.

# Sample Inputs:

# hello -> True
# nono -> False
# sunday -> False
# racecar -> False

# word = 'hello'
def double_letters(word):
    for letter in range(1, len(word)):
        if word[letter] ==  word[letter - 1]:
            return True

    return False
double_letters('hello')
        
    
    
# Converting Numpy Array Datatypes
# The following list represents tempuratures in New York

tempuratures = ['76.5', '79.1','80.3', '78.3','75.6', '73.2']

# Write a function that takes reads a string list of tempuratures
# Convert that string list into a list of floats and calculate the average
# Hints:
# use .astype()

import numpy as np
import math

def avg(seq):
    x = np.array(tempuratures).astype(float)
    return round(np.mean(x), 2)
avg(tempuratures)
