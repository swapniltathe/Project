def add(x, y):
    return x + y


def subtract(x, y):
    if x < y:
        x, y = y, x
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if x < y:
        x, y = y, x
    return x / y


def filemod(x):
    x = str(oct(x)[2:])
    perm = ['?']
    all_perm = {0: "---", 1: "--x", 2: "-w-", 3: "-wx", 4: "r--", 6: "r-x", 6: "rw-", 7: "rwx"}
    if len(x) == 3:
        for i in x:
            if int(i) in all_perm.keys():
                perm += all_perm.get(int(i))
    else:
        for i in x[1:]:
            if int(i) in all_perm.keys():
                perm += all_perm.get(int(i))
        if x[0] == '1':
            perm[9] = 'T' if int(x[3]) % 2 == 0 else 't'
        if x[0] == '2':
            perm[6] = 'S' if int(x[2]) % 2 == 0 else 's'
        if x[0] == '3':
            perm[9] = 'T' if int(x[3]) % 2 == 0 else 't'
            perm[6] = 'S' if int(x[2]) % 2 == 0 else 's'
        if x[0] == '4':
            perm[3] = 'S' if int(x[1]) % 2 == 0 else 's'
        if x[0] == '5':
            perm[3] = 'S' if int(x[1]) % 2 == 0 else 's'
            perm[9] = 'T' if int(x[3]) % 2 == 0 else 't'
        if x[0] == '6':
            perm[3] = 'S' if int(x[1]) % 2 == 0 else 's'
            perm[6] = 'S' if int(x[2]) % 2 == 0 else 's'
        if x[0] == '7':
            perm[3] = 'S' if int(x[1]) % 2 == 0 else 's'
            perm[6] = 'S' if int(x[2]) % 2 == 0 else 's'
            perm[9] = 'T' if int(x[3]) % 2 == 0 else 't'
    return ''.join(perm)
"""
import os

# print(os.getcwd())
# os.chdir("/root")
# print(os.getcwd())
# print(os.listdir())
#########################

try:
    filename = 'script.py'
    file = open(filename, 'r+')
    text = file.read()
    file.close()
    print(2 / 0)

except ZeroDivisionError:
    print("Error: trying to divide by zero.")

except IOError:
    print("Error: \n\t  {} file not found".format(filename))

# Nested list
# my_list = [1, [2, 3, 4, [6, 7]], 5]
# print(my_list[1][3][1])

my_list = [0, 1, 2, 3, 4, 5, 6]
# print(my_list[2:5])  # will print from 2nd index till 4th index position
# print(my_list[:5])  # will print from beginning till 4th index position
# print(my_list[:])  # will print all values

# my_list[0] = 7  # updating 0 index position value
# print(my_list)

# my_list[1:5] = [8, 9, 10, 11]  # updating values from 1st till 4th index position
# print(my_list)

# my_list.insert(0,34)
# print(my_list)

del my_list[0]  # to delete value from index 0
# or use below
my_list.pop(0)  # alternate to del
print(my_list)


# Print Pyramid
# p = int(input("Enter Pyramid rows: "))
pyramid_rows = 4
right_mark = 0
current_row = 1

while current_row <= pyramid_rows:
    space_mark = right_mark
    while space_mark <= pyramid_rows:
        print(end=" ")
        space_mark += 1

    left_mark = 1
    while left_mark <= current_row:
        print(end="*")
        left_mark += 1

    right_mark = 1
    while right_mark < current_row:
        print(end="*")
        right_mark += 1

    current_row += 1
    print("\r")


# Another Pyramid
def triangle(n):
    # number of spaces
    k = 2 * n - 2

    # outer loop to handle number of rows
    for i in range(0, n):

        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")

        # decrementing k after each loop
        k = k - 1

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")

        # ending line after each row
        print("\r")

    # Driver Code


n = 5
triangle(n)

# Counter

i = 1
while i <= 3:
    print("Row: {}".format(i))
    i += 1

j = 3
for i in range(0, j):
    print("Row: {}".format(i))


# Break will stop 'for' and 'while' loop if condition is True
for i in "string":
    if i == "i":
        break
    print(i)
print("The End.")

# Continue will skip loop if condition is True
for i in "string":
    if i == "i":
        continue
    print(i)
print("The End.")

def adder(**num):
    #sum = 0
    #for i in num:
        #sum = sum + i
    #return sum
    print(num)
    for var, value in num.items():
        print("{} is {}".format(var, value))


adder(Name="Swapnil", Age=100)

print(bin(25))
print(0b11001)
print(oct(25))
print(0o31)
print(hex(25))
print(0x19)

a = 52
print(bin(5), bin(6))
b = 61
print(a,b)
# a, b = b, a
a = a ^ b
print(a, b)
b = a ^ b
print(a, b)
a = a ^ b
print(a, b)

# a = 101
# b = 110
# ===========
#     011
# print(0b011)

# Bitwise Operators
# print(~45)  # complement of number
# print(12 & 13)  # and operator  1100 & 1101 = 1100 (1+1=1, 1+0=0, 0+1=0, 0+0=0)
# print(12 | 13)  # or operator   1100 | 1101 = 1101 (1+1=1, 1+0=1, 0+1=1, 0+0=0)
# print(12 ^ 13)  # xor operator  1100 ^ 1101 = 0001 (1+1=0, 1+0=1, 0+1=1, 0+0=0) even numbers become zero
print(10 << 2)  # Left shift operator. Original number in bin 1010.00 left shift 2 will add two zeros i.e. 101000.
print(10 >> 2)  # Right shift operator. Original number in bin 1010.00 right shift 2 will remove two zeros i.e. 10.1000


# Factorial number means factorial of 5 will be 5 * 4 * 3 * 2 * 1 = 120
def fact(x):
    fac = 1
    for i in range(1, x + 1):
        fac = fac * i
    return fac


num = int(input("Enter number: "))
print("Factorial number: {}".format(fact(num)))

######################

# Recursion means executing same funtion within it
import sys

print(sys.getrecursionlimit())  # check limit of recursion limit
sys.setrecursionlimit(2000)  # Change recursion limit
print(sys.getrecursionlimit())

# Example
def sayhello():
    print("Hello")
    sayhello()

sayhello()
#####################

# Recursion funtion to get Factorial number
def fac(n):
    if n == 0:
        return 1
    return n * fac(n-1)


result = fac(1)
print(result)
#####################

# Lambda functions / anonymous function / function without name
def sqr(x):
    return x * x
print(sqr(5))

# OR same in lambda
sqare = lambda x: x * x
print(sqare(5))

#Other Lambda examples

f = lambda a, b: (a + b) / 2

print(f(5, 6))
######################

from functools import reduce

# def evensf(x):
#     lst = []
#     for i in x:
#         if i % 2 == 0:
#             lst.append(i)
#     return lst
#
nums = [2, 5, 6, 1, 3, 4, 8, 7]
#
# result = evensf(nums)
# print(result)

evens = list(filter(lambda x: x % 2 == 0, nums))  # filter will verify for True condition and print passed values
print(evens)

doubles = list(map(lambda x: x * 2, evens))  # map will perform operation on single value at time and print values as
                                             # lst
print(doubles)

sums = reduce(lambda x, y: x + y, doubles)  # reduce will perform operation on two values at time and print single value
print(sums)
#######################

# Google First program
# def find4(x):
#     if x == 4:
#         return x - 1
#     else:
#         return x

def getcheques(x):
    if "4" in x:
        x_lst = [int(i) for i in str(x)]
        # print(x_lst)
        #f_chek_lst = list(map(find4, x_lst))
        f_chek_lst = list(map(lambda j: j-1 if j == 4 else j, x_lst))
        #print(f_chek_lst)
        a = int(str(f_chek_lst).strip('[]').replace(', ', ''))
        b = int(x) - a
        return a, b


amount = input()
if "4" not in amount:
    exit(0)
# amount = "1843"
cheque1, cheque2 = getcheques(amount)
print(cheque1, cheque2)

## WORKING ON GOOGLE


def getcheques(x):
    if "4" in x:
        x_lst = [int(i) for i in str(x)]
        f_chek_lst = list(map(lambda j: j-1 if j == 4 else j, x_lst))
        a = int(str(f_chek_lst).strip('[]').replace(', ', ''))
        b = int(x) - a
        return a, b


casex = int(input())
for i in range(1, casex + 1):
    amount = input()
    if "4" not in amount:
        continue
    cheque1, cheque2 = getcheques(amount)
    print("Case #{}: {} {}".format(i, cheque1, cheque2))

### py2 program from google topper
t = int(raw_input())


def solve():
    s = raw_input()
    a = ""
    for i in xrange(len(s)):
        if s[i] == '4':
            a += '1'
        else:
            a += '0'
    return "%s %s" % (int(a), int(s) - int(a))


for __ in xrange(t):
    print "Case #%d: %s" % (__ + 1, solve())

########## improved google code
def getcheques(x):
    if "4" in x:
        x_lst = [int(i) for i in str(x)]
        f_chek_lst = list(map(lambda j: j-1 if j == 4 else j, x_lst))
        a = str(f_chek_lst).strip('[]').replace(', ', '')
        b = int(x) - int(a)
        return a, b
    else:
        return x, 0


casex = int(input())
for i in range(1, casex + 1):
    amount = input()
    cheque1, cheque2 = getcheques(amount)
    print("Case #{}: {} {}".format(i, cheque1, cheque2))
#######################
# Google Code Jam 2019 qualify round #2 question
def funct():
    grid = int(input())
    path = input()
    result = []
    for j in range((2 * grid) - 2):
        result.append('E' if path[j] == 'S' else 'S')
    return ''.join(result)


casex = int(input())
for i in range(casex):
    print("Case #{}: {}".format(i + 1, funct()))
#########################


# Convert list containing only string
lst = ["A", "B", "C", "D"]
print(''.join(lst))
# Convert list containing mixed data
lst = [1, "s", 'hello', 4]
print(str(lst).strip("[]").replace(", ", "").replace("'", ""))
################
# Google code jam 3rd question - qualify round 2019
# alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# k = 0
# for i in range(3, 104):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(alpha[k], "=", i, end=" || ")
#         k += 1
#
# print()
# print(61 * 31)
lst = []
in_lst = list(input().split(" "))
j = 3
for i in in_lst:
    i = int(i)
    while True:
        if i % j == 0:
            break
        else:
            j += 1
    q = int(i) / j
    q = int(q)
    lst.extend([j, q])
print(lst)

############################
# Password request form + update server name
lst = list(input("Enter servers: ").split(" "))
matter = "Requester - 8100404\nServer/Host/Domain - {}\nAccount - root\nAccount - tslemerg"

for i in lst:
    if i == lst[0]:
        print("Please provide the Password for below File Id.")
        print(matter.format(i), end='\n\n')
    elif i == lst[-1]:
        print(matter.format(i))
    else:
        print(matter.format(i), end='\n\n')

############################
# Decorators used to modifying functionality of original function.
def div(a, b):
    print(a / b)


def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner


div = smart_div(div)
print(div(5, 10))
############################
"""
# __name__ variable: Import this file from different file and it will tell this file name there

if __name__ == "__main__":
    print("Hello", __name__)
###########################
### From Home PC all.py ###
###########################
"""
import random
import os

cm_in_inch = 2.54
inch_in_feet = 12
km_in_mile = 1.60934
feet_in_mile = 5280


def get_file_ext(filename):
    basename, file_extension = os.path.splitext(filename)
    return file_extension


def roll_dice(num):
    return random.randint(1, num)


from math import *

# List = []  # exp. FRNDS = ["Swapnil", 2, True, "Maatu", 5]
# Tuples = ()  # exp. FRNDS = ("Swapnil", 2, True, "Maatu", 5)
# Dictionary = {}  # exp. Months = {
#     "Jan": "January",
#     2: "February",
#     "Mar": "March"
# }

# Print hello
print("Hello World1!")
# Variable2
CHAR_NAME 3 "Swapnil"  # String variable
CHAR_AGE =433  # Numeric variable
print("Th was man named " + CHAR_NAME + ",")
print(CHAR_NAME + "'s age is " + str(CHAR_AGE) + " years old.")  # Need to add str() to print number
print(CHAR_NAME.upper())
print(CHAR_NAME.upper().isupper())
print(len(CHAR_NAME))
print(CHAR_NAME[0])  # 0 will print character present at 0 location i.e S in variable, 1 will print w
print(CHAR_NAME.index("S"))  # S will print its location in variable i.e 0
print(CHAR_NAME.replace("Swa", "Qwa"))
# Arithmetic operations
print(3 + 4)  # addition
print(4 - 3)  # subtraction
print(4 * 3)  # multiplication
print(4 / 2)  # division
print(4 % 3)  # mod/exponential/reminder of division
print(4 * 2 + 5)  # complex addition
print(4 * (2 + 5))  # using parenthesis
print(abs(-5))  # getting absolute value
print(pow(3, 2))  # getting power of number 3 ^ 2 i.e 3x3=9
print(max(3, 6))  # finding bigger number
print(min(3, 6))  # finding smaller number
print(round(5.3))  # round the number to 5
print(round(5.7))  # round the number to 6
print(floor(5.7))  # chop off .7 number (Only available after importing math in line 1)
print(ceil(5.3))  # consider bigger number during round off numbers here 6
print(sqrt(49))  # square root of 49 is 7
# Take input
NAME = input("Enter your name: ")
print("Hello " + NAME + "!")
NUM1 = input("Enter first number: ")
NUM2 = input("Enter second number: ")
result = float(NUM1) + float(NUM2)
print(result)
NUM1 = float(input("Enter first number: "))
NUM2 = float(input("Enter second number: "))
print("Addition of", NUM1, "and", NUM2, "is", NUM1 + NUM2)
print("Subtraction of", NUM2, "from", NUM1, "is", NUM1 - NUM2)
print("Multiplication of", NUM1, "and", NUM2, "is", NUM1 * NUM2)
print("Division of", NUM1, "by", NUM2, "is", NUM1 / NUM2)
# List
FRNDS = ["Swapnil", 2, True, "Maatu", 5]
print(FRNDS[0])
print(FRNDS[2:])  # will print all value from position 2
print(FRNDS[2:3])  # Will not print 3rd position value
print(FRNDS[-1])  # will print last value
print(FRNDS[-2])  # will print second last value
FRNDS[0] = "Komal"  # Updating position with diff. value
print(FRNDS[0])
FRNDS = ["Komal", "Viraj", "Swapnil", "Akshay"]
LUCKY_NUM = [67, 2, 3, 135, 34]
FRNDS.extend(LUCKY_NUM)  # add one list to other
FRNDS.append("Sandy")  # add item to list
FRNDS.insert(1, "Mayur")  # insert item in list on particular position
FRNDS.remove("Swapnil")  # remove item from list
FRNDS.clear()  # to remove all items from list
FRNDS.pop()  # removes last item from the list
print(FRNDS)
print(FRNDS.index("Akshay"))  # to find name is in list or not
print(FRNDS.count("Komal"))  # to find how many Komal values in list
FRNDS.sort()  # to sort values a-z
print(FRNDS)
LUCKY_NUM.sort()  # to sort numbers in ascending
print(LUCKY_NUM)
LUCKY_NUM.reverse()  # to sort numbers in descending
print(LUCKY_NUM)
FRNDS.reverse()  # to sort values z-a
print(FRNDS)
FRNDS2 = FRNDS.copy()  # to create copy of list
print(FRNDS2)
# Tuples
# They are like List but major diff. is they can't be modified and we use () to define them
NUM = (11, 3, 67, 25)
print(NUM[-1])
# Function
def say_hi(name, age):
    print("Hi " + name + "! \n\tyour age is " + age + "\n")
say_hi("Swapnil", "33")
say_hi("Komal", "27")
# Return function
def cube(num):
    return num * num * num
print(cube(3))
# If statement
is_male = False
is_tall = True
if is_male or is_tall:
    print("You are male or tall or both!")
else:
    print("You neither male nor tall!")

if is_male and is_tall:
    print("You are tall male!")
elif is_male and not(is_tall):
    print("You are Short male!")
else:
    print("You either not male or not tall or both!")
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(1, 3, 22), "is big number")
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Error: Invalid operator\n\tValid operators: + - * /")
# Dictionary
Months = {
    "Jan": "January",
    2: "February",
    "Mar": "March"
}
print(Months["Jan"])
print(Months.get("Mar"))
print(Months.get(2))
print(Months.get("Lan"))
print(Months.get("Lan", "Invalid Month"))

# While loop
i = 1
while i <= 10:
    print(i)
    i += 1  # shorthand of i = i + 1

secret_ans = "komal"
guess = ""
guess_count = 0

while guess != secret_ans and guess_count < 3:
    guess = input("Name of my Love: ")
    guess_count += 1

print("Correct Its Komal!")

secret_ans = "Komal"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_ans and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Name of my Love: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, You Lose!")
else:
    print("Correct, You Win!")

# For loop
for letter in "Komal Tathe":
    print(letter)

friends = ["Komal", "Viraj", "Swapnil"]
for friend in friends:
    print(friend)

for number in range(10):
    print(number)

for number in range(3, 10):
    print(number)

friends = ["Komal", "Viraj", "Swapnil"]
for index in range(len(friends)):
    print(index, friends[index])

for index in range(5):
    if index == 0:
        print("First iteration")
    elif index == 4:
        print("Last iteration")
    else:
        print("Not first")

# Exponent function
print(2**3)
# Create same exponent function using loop
def rise_to_power(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result = result * base_num
    return result
print(rise_to_power(2, 3))

# 2D lists & Nested loops
# Creating grid
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[0][0])
print(number_grid[1][2])
print(number_grid[2][1])

for row in number_grid:
    print(row)
    for column in row:
        print(column)

# Build a translator
def translate(phase):
    translation = ""
    for letter in phase:
        if letter.lower() in "aeiou":
        # if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase: ")))

# Try Except
# To avoid breaking program if user input invalid data
try:
    # value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
# except ZeroDivisionError:
#    print("Divided by Zero")
except ValueError as err:
    print(err)
# except ValueError:
#    print("Error: Invalid Inputs")

# reading files
# open("data.txt", "r")  # to open file in read only mode
# open("data.txt", "r+")  # to open file in read and write mode
# open("data.txt", "w")  # to open file in write mode
# open("data.txt", "a")  # to open file in append mode, which will not modify existing data

data_file = open("data.txt", "r")
# print(data_file.readable())  # to check if file is readable or not
# print(data_file.read())  # to read entire file content
# print(data_file.readline())  # to read file line by line on every encounter
# print(data_file.readline())  # 2nd encounter of readline
# print(data_file.readlines())  # add lines to list
# print(data_file.readlines()[1])  # to print second row in file
for relative in data_file.readlines():
    print(relative)

data_file.close()
# Writing to file
# data_file = open("data.txt", "a")
# data_file.write("\nJanardhan - cousin")
# data_file.close()

# data_file = open("data.txt", "w")  # w will replace all text in file
# data_file.write("\nJanardhan - cousin")
# data_file.close()

# Create new file
data_file = open("data.html", "w")
data_file.write("<p>Hello Guys, this is new file</p>")
data_file.close()

# Modules and pip
import useful_functions
import os
# print(useful_functions.roll_dice(10))
print(useful_functions.get_file_ext("C:\abc\PycharmProjects\Python.txt"))

filename, file_extension = os.path.splitext("/usr/local/script.ksh")
file_extension = os.path.splitext("/usr/local/script.ksh")[1]
print(file_extension)
##########################################################
# Unix python scripts

import sys

if __name__ == "__main__":
    names = {}
    for name in sys.stdin.readlines():
            name = name.strip()
            if name in names:
                    names[name] += 1
            else:
                    names[name] = 1

    for name, count in names.iteritems():
            sys.stdout.write("%d\t%s\n" % (count, name))


#!/usr/bin/env python3
import sys


if __name__ == "__main__":
    # Initialize a names dictionary as empty to start with.
    # Each key in this dictionary will be a name and the value
    # will be the number of times that name appears.
    names = {}
    # sys.stdin is a file object. All the same functions that
    # can be applied to a file object can be applied to sys.stdin.
    for name in sys.stdin.readlines():
        # Each line will have a newline on the end
        # that should be removed.
        name = name.strip()
        if name in names:
            names[name] += 1
        else:
            names[name] = 1
    # Iterating over the dictionary,
    # print name followed by a space followed by the
    # number of times it appeared.
    # for name, count in names.iteritems():  # works only for python2
    for name, count in names.items():
        print("%d\t%s" % (count, name))
        # print(str(count)+"\t"+name)  # alternate for above line
        # sys.stdout.write("%d\t%s\n" % (count, name))  # alternate function for print function

#!/usr/bin/env python3
import csv
import sys


if __name__ == "__main__":
    # The CSV module exposes a reader object that takes
    # a file object to read. In this example, sys.stdin.
    csvfile = csv.reader(sys.stdin)

    # The script should take one argument that is a column number.
    # Command-line arguments are accessed via sys.argv list.
    column_number = 0
    if len(sys.argv) > 1:
        column_number = int(sys.argv[1])

    # Each row in the CSV file is a list with each
    # comma-separated value for that line.
    for row in csvfile:
        print(row[column_number])
######################


from pathlib import Path
import datetime


def date(format="%Y%m%d"):
    return datetime.datetime.utcnow().strftime(format)


def make_output_dir() -> Path:
    today = date("%Y%m%d")
    output_dir = Path(".") / f"results_{today}"
    output_dir.mkdir(exist_ok=True)
    return output_dir


p = Path('.')
print(p.absolute())
print(p.absolute().as_uri())  # makes path like windows file:///blah~blah
print(p.absolute().parent)  # to get parent directory
print(p.exists())
print(p.is_dir())
print(p.is_file())

q = p / 'newdir'  # can create variable with newdir directory path
print(q.absolute())
print(q.exists())
print(q.is_dir())
print(q.is_file())


DATE = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
print(DATE)
######################

# Unix Commands
import subprocess
import os

output = subprocess.getoutput('ls')
print(output)
num = output.count('d')  # will count how many times letter 'd' occurred in output variable
print(num)

print("hello this is python")
os.system("echo 'hello this is bash'")
os.system("ls -ltr")
########################


import os
# Rename multiple files in directory
os.chdir('/media/sf_share/python_scripts/rename_multiple_files')  # to change current working directory
# os.chdir(r"D:\Softwares\VM\RHEL7\share\python_scripts\rename_multiple_files")  # to change windows current working dir
# print(os.getcwd())  # to print current working directory

for f in os.listdir():
    # print(f)
    f_name, f_ext = os.path.splitext(f)  # Separating file name and file extension
    f_title, f_num = f_name.split('-')  # further spliting file name considering '-' as separator
    # print(f_title)
    f_title = f_title.strip()  # to remove white spaces from begging and ending of file name
    # f_num = f_num.strip()
    # f_num = f_num.strip()[1:]  # to remove starting '#' character, will print from 2nd till end
    f_num = f_num.strip()[1:].zfill(2)  # To change starting number from 1,2,3 to 01,02,03
                                        # so 10 will not play after 1 file
    # print('{}-{}{}'.format(f_num, f_title, f_ext))  # to create file name like number first then planet name then extn
    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)  # setting new file name to var
    os.rename(f, new_name)  # to rename actual files in directory


var = " Hello "
var = var.strip().split(sep="e")[1]
print(var)

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

a, b = 0, 1
for i in range(0, 10):
    print(a)
    a, b = b, a + b

a = 1
b = 2
c = 1

for i in range(1, 11):
    print(a)
    c = a
    a = b
    b = c + b

print('Swapnil\'s "Laptop"')
print(r'C:\docs\navin')  # to print RAW string
name = 'Swapnil Tathe'
print(len(name))
List = [1, 2, 3]
List[0] = 4
print(List)

Tuple = (1, 2, 3)
print(Tuple)

Set = {98, 12, 22, 3, 98}
print(Set)



# num = 5
# print(id(num))
#
# var = 5
# print(id(var))
# name = 'swapnil'
#
# print(id(name))
#
# sel = 'swapnil'
# print(id('swapnil'))
#
# name = None
# print(type(name))
#
# print(int(True))
# print(int(False))

# print(list(range(10)))
# print(list(range(2, 11, 2)))  # to find even numbers between 2 and 10 numbers

# d = {'swapnil': 'Poco F1', 'komal': 'Samsung galaxy max', 'viraj': 'No mobile'}
# print(d.keys())
# print(d.values())
# print(d['swapnil'])
# print(d.get('komal'))

print(bin(25))
print(hex(25))
print(oct(25))
print(0b11001)

import math as m

print(m.sqrt(25))
print(m.floor(2.9))
print(m.ceil(2.2))
print(m.pow(3, 2))
print(m.pi)
print(m.e)


from math import sqrt, pow
print(sqrt(25))
print(pow(2, 3))

result = eval(input("Enter Expression: "))
print(result)
# 5 - 2 + 7 * 4 / 2
# 5 - 2 + 8 / 4 * 2

from sys import argv

x, y = int(argv[1]), int(argv[2])
print(x + y)

a = 1
while a <= 5:
    print(end="Swapnil ")
    b = 4
    while b >= 1:
        print(end="Rocks! ")
        b -= 1
    print("\r")
    a += 1

# Multiplication table 1 to 10
a = 1
while a <= 10:
    b = 1
    while b <= 10:
        var = str(a * b)
        print(var.zfill(2), end=" ")
        b += 1
    print("\r")
    a += 1

# Count 1 to 10
for i in range(1, 11, 1):
    print(i)

# Reverse count 10 to 1
for i in range(10, 0, -1):
    print(i)

for i in range(1, 21):
    if i % 5 != 0:
        print(i)
    else:
        print(i, "is divisible by 5")

def vending():
    try:
        x, y = input("What do you want?\ncandy or banana: "), int(input("How many? "))
    except ValueError:
        print("\tError: Please enter valid quantity")
        exit()
    y += 1
    if x.lower() == "candy" or x.lower() == "banana":
        for i in range(1, y):
                print(i, "x", x, end=" || ")
    else:
        print("\tError: Wrong Selection! \n\t\tPlease select either 'candy' or 'banana'!")


vending()

# Print odd numbers using pass

for i in range(1, 101):
    if i % 2 == 0:
        pass
    else:
        print(i)

# Printing patterns
for i in range(4):
    for j in range(4):
        print(end="# ")
    print("\r")

for i in range(4):
    for j in range(i + 1):
        print(end="# ")
    print("\r")

for i in range(4, 0, -1):
    for j in range(i):
        print(end="# ")
    print("\r")
# Alternate for above
for i in range(4):
    for j in range(4 - i):
        print(end="# ")
    print("\r")

# For else loop
nums = [2, 3, 45, 19, 36]

for i in nums:
    if i % 5 == 0:
        print(i)
        break  # Break is important, else it will print else: statement as well
else:
    print("No value divisible by 5!")

# find prime number(prime number is divisible by 1 and itself i.e 7)
#num = int(input("Enter number: "))
for num in range(1, 101):
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print(num, "is Prime!")

# Find prime numbers efficient way
from math import sqrt
for num in range(1, 101):
    for i in range(2, int(sqrt(num) + 1)):  # efficient way
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print(num, "is Prime!")

# Array
from array import *
vals = array('i', [2, 8, 34, 6, 1])
# newarr = array(vals.typecode, (a for a in vals))  # To copy array to new array
newarr = array(vals.typecode, (a * a for a in vals))  # To copy array and convert value to sqrt
# vals = array('u', ['a', 'e', 'i', 'o', 'u'])
# print(vals)
print(newarr)
# print(vals.buffer_info())
# print(vals.typecode)
# vals.reverse()
# print(vals)
# print(vals[0])

for i in vals:
    print(i)
# OR
a = 0
while a < len(vals):
    print(vals[a])
    a += 1

# Creating array from user inputted values
from array import *
arr = array('i', [])  # Define blank array
n = int(input("Enter length of Array: "))

for i in range(n):
    x = int(input("Enter next value: "))
    arr.append(x)

print(arr)

val = int(input("Enter value for search: "))
k = 0
for e in arr:
    if val == e:
        print(k)
        break
    k += 1
else:
    print("Error: Value not found in array!")
# OR simply by function
print(arr.index(val))

from numpy import *

# arr = array([1, 2, 3], int)
# or
arr = array([12, 2, 4])
print(arr)
# Adding value to all array elements
arr = arr + 3
print(arr)
# Adding to arrays
arr2 = array([4, 7, 3])
print(arr2)
arr3 = arr + arr2
print(arr3)
# Maths on arry
print(sin(arr))
print(cos(arr))
print(tan(arr))
print(sqrt(arr))
print(sum(arr))
print(min(arr))
print(max(arr))
print(sort(arr))
print(concatenate([arr, arr2]))

# Copying array
arr3 = arr  # This will simply alias the array
print(id(arr), id(arr3))
print(arr, arr3)

arr3 = arr.view()  # This is shallow copy means if original array value changed, will change arr3 array value as well
print(id(arr), id(arr3))
arr[1] = 3
print(arr, arr3)
arr[1] = 2  # Reverting changes of arr array

arr3 = arr.copy()  # This is deep copy, will have no link with original array after copy
print(id(arr), id(arr3))
arr[1] = 3
print(arr, arr3)

arr1 = array([
        [1, 2, 3, 6, 9, 2],
        [4, 5, 6, 1, 5, 3]
            ])

print(arr1)
print(arr1.dtype)  # data-type int or float or string
print(arr1.ndim)  # dimension of array 2 means two dimension array
print(arr1.shape)  # gives tuple number of rows and columns
print(arr1.size)  # Size of entire block or number of values in array
arr2 = arr1.flatten()  # creating arr2 by converting two dimensional array to single dimensional
print(arr2)
arr3 = arr2.reshape(3, 4)  # Converting 1d array to 2d. 3 = rows 4 = columns
print(arr3)
arr4 = arr2.reshape(2, 2, 3)  # Converting 1d array to 3d. 2 = no. of 2d arr, 2 = no. of 1d array, 3 = no. of values
print(arr4)

# Matrix

# m = matrix('1 2 3 4; 5 6 7 8')
# print(m)

m = matrix('1 2 3; 4 5 6; 7 8 9')
print(m)

print(m.diagonal())  # To print diagonal values in matrix
##############
def greet(name):
    print("Hello {},\n\tWelcome to Class!".format(name))


greet(input("Enter Name: "))
###########

# Multiple values return
def add_sub(x, y):
    a = x + y
    s = x - y
    return a, s


result1, result2 = add_sub(5, 2)
print(result1, result2)
###############

# Passing keywords and argument in function
def person(name, age):  # name and age are keywords
    print("Hello {}!\n\tYour age is {}.".format(name, age))


person(age=33, name='Swapnil')  # name and age are keywords and 33 and Swapnil are arguments
###############

# Passing Default arguments
def person(name, age=18):  # age will take default value if not provided by user
    print("Hello {}!\n\tYour age is {}.".format(name, age))


person('Swapnil')  # Not passing argument for age keyword
person('Swapnil', 33)  # Passing argument for age keyword
###############

# Variable length argument in function
def add(*num):
    sums = 0
    for i in num:
        sums += i
    print(sums)

add(1, 2, 3, 4, 5, 6, 7, 8, 9)
###############

# Kwargs in function
def person(**data):
    for i, j in data.items():
        print("{} is {}".format(i, j))


person(name='Swapnil', age=33, city='Pune', mobile=9920115341)
###############

# Global variable
a = 10
def something():
    # global a  # To change value of global variable
    a = 15
    x = globals()['a']  # Setting global varialbe a's value to variable x
    print(x)
    print("Inside function:", a)
    globals()['a'] = 20  # Changing global variable's value from inside

something()
print("Outside:", a)
###############

# Segregate odd and even number and show count
def check(lst):
    even = []
    even_count = 0
    odd = []
    odd_count = 0
    for i in lst:
        if i % 2 == 0:
            even.append(i)
            even_count += 1
        else:
            odd.append(i)
            odd_count += 1
    return even, even_count, odd, odd_count


lst = eval(input("Enter numbers by comma separated: "))

even, even_count, odd, odd_count = check(lst)
print("\tEven numbers: {} (Count: {})\n\tOdd numbers: {} (Count: {})".format(str(even).strip('[]'), even_count, str(odd).strip('[]'), odd_count))
###############

# Fibonacci Sequence, enter number of sequences
n = int(input("Enter number: "))
a, b = 0, 1
for i in range(0, n):
    print(a)
    a, b = b, a + b

# Print Fibonacci sequence till user provided last number
n = int(input("Enter last number: "))
a, b = 0, 1
while True:
    if a <= n:
        print(a)
        a, b = b, a + b
    else:
        break
###############

from functools import reduce

# Without lambda
# def is_evens(x):
#     return x % 2 != 0
# nums = [7, 2, 5, 6, 4, 3, 8, 1]
# result = list(filter(is_evens, nums))  # filter need function which will return True/False bullion only
# print(result)

# With Lambda
nums = [7, 2, 5, 6, 4, 3, 8, 1]
evens = list(filter(lambda x: x % 2 == 0, nums))  # filter will pass only True values from nums list to evens list
print(evens)

doubles = list(map(lambda x: x * 2, evens))  # map will perform modification on single values
print(doubles)

sums = reduce(lambda x, y: x + y, doubles)  # reduce will convert list to integer by performing repetitive function on /
                                            # values
print(sums)
###############


def div(x, y):
    print(x / y)


def smart_div(func):

    def inner(x, y):
        if x < y:
            x, y = y, x
        return func(x, y)

    return inner


result = smart_div(div)
result(2, 22)
#############################

# Rotate list to get day of 1st day 1st month of year
from math import floor
yrs = 2118
days = ["tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "monday"]
div = floor((yrs - 2001) / 4)
# print(div)
st_cnt = 1
ed_cnt = (yrs - 2001) + div
# print(ed_cnt)
i = 0
while st_cnt != ed_cnt:
    if i == 6:
        i = -1
    st_cnt += 1
    i += 1
print(days[i])

# import calendar
# n = 2118
# t = calendar.weekday(n, 1, 1)
# if t == 0:
#     print("monday")
# elif t == 1:
#     print("tuesday")
# elif t == 2:
#     print("wednesday")
# elif t == 3:
#     print("thursday")
# elif t == 4:
#     print("friday")
# elif t == 5:
#     print("saturday")
# else:
#     print("sunday")
##############################

# Get day of any date
def cent(x):  # to get first two digits of int = year ie. 1992 = 19
    while x >= 100:
        x = x / 100
    return int(x)


date = list(input("Enter Date (format: D-M-YYYY): ").split("-"))
# date = [3-7-1986]
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
f_day = int(date[0])
# print("f_day: ", f_day)
month = int(date[1])
# print(month)
year = int(date[2])
if len(str(year)) != 4:
    print("Error: Year Out of Range!")
    exit(1)
yer = year % 100
cen = int(str(cent(year))+"00")
# print(cen, yer)

# find year code
yer_code = int((yer + (yer / 4)) % 7)
# print("yer_code: ", yer_code)

# find month code
if month <= 0 or month > 12:
    print("Error: Incorrect month!")
    exit(1)
mnt_lst = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
mon_code = mnt_lst[month - 1]
# if month == 1:
#     mon_code = 0  # Jan = 0
# elif month == 2:
#     mon_code = 3  # Feb = 3
# elif month == 3:
#     mon_code = 3  # Mar = 3
# elif month == 4:
#     mon_code = 6  # Apr = 6
# elif month == 5:
#     mon_code = 1  # May = 1
# elif month == 6:
#     mon_code = 4  # Jun = 4
# elif month == 7:
#     mon_code = 6  # Jul = 6
# elif month == 8:
#     mon_code = 2  # Aug = 2
# elif month == 9:
#     mon_code = 5  # Sep = 5
# elif month == 10:
#     mon_code = 0  # Oct = 0
# elif month == 11:
#     mon_code = 3  # Nov = 3
# elif month == 12:
#     mon_code = 5  # Dec = 5
# else:
#     print("Error: Incorrect month!")
#     exit(1)
# print("mon_code: ", mon_code)

# finding century code
lst = [2, 0, 6, 4]
st_cnt = 1000
ed_cnt = cen
i = 0
while st_cnt != ed_cnt:
    if i == 3:
        i = -1
    st_cnt += 100
    i += 1
# print("cen: ", cen, lst[i])
cen_code = lst[i]

# 1000 = 2
# if cen == 1600:
#     cen_code = 6
# elif cen == 1700:
#     cen_code = 4
# elif cen == 1800:
#     cen_code = 2
# elif cen == 1900:
#     cen_code = 0
# elif cen == 2000:
#     cen_code = 6
# elif cen == 2100:
#     cen_code = 4
# elif cen == 2200:
#     cen_code = 2
# elif cen == 2300:
#     cen_code = 0
# elif cen == 2400:
#     cen_code = 6
# elif cen == 2500:
#     cen_code = 4
# else:
#     print("Error: Year Out of Range!")
#     exit(1)
# print("cen_code: ", cen_code)

# Checking leap year
if year % 400 == 0:
    if month == 1 or month == 2:
        leap = -1
    else:
        leap = 0
elif year % 100 == 0:
    leap = 0
elif year % 4 == 0:
    if month == 1 or month == 2:
        leap = -1
    else:
        leap = 0
else:
    leap = 0
# print("leap: ", leap)
# print(yer_code, mon_code, cen_code, f_day, leap)
day_code = ((yer_code + mon_code + cen_code + f_day + leap) % 7)
print("Day: ", days[day_code])
############################

# Class
class Computer:
    def config(self):  # behaviour of class aka method(old name: function)
        print("8GB RAM, 4 CPU, 250GB Disk")


# Defining com1 and com2 as attributes/variables of Computer class
com1 = Computer()
com2 = Computer()

Computer.config(com1)
Computer.config(com2)
# OR we can write above as below
com1.config()
com2.config()
############################

class Computer:
    def __init__(self, cpu, ram):  # run on every object without calling
        self.proccessor = cpu
        self.memory = ram

    def config(self):  # behaviour of class aka method(old name: function)
        print("config is: ", self.proccessor, self.memory)


com1 = Computer('i5', 8)
com2 = Computer('Ryzen5', 16)

com1.config()
com2.config()
###########################

class Computer:
    def __init__(self):
        self.name = "Swapnil"
        self.age = 33

    def update(self):
        self.age = 40

    def compare(self, other):
        return True if self.age == other.age and self.name == other.name else False


c1 = Computer()  # Computer() is constructor who allocates size/memory to object c1 depending upon args
c2 = Computer()
print(c1.name, c1.age)
print(c2.name, c2.age)

if c1.compare(c2):
    print("They are same!")
else:
    print("They are diff!")

c2.name = "Komal"
c2.age = 27
print(c1.name, c1.age)
print(c2.name, c2.age)

if c2.compare(c1):
    print("They are same!")
else:
    print("They are diff!")

c1.update()
print(c1.name, c1.age)
print(c2.name, c2.age)
##################################

class Car:
    wheels = 4  # These variables are Class/Static variables because they are not in __init__ method and inside class

    def __init__(self):
        self.mil = 10  # These variables called Instance variables because they can be changed for every object
        self.com = "BMW"


c1 = Car()  # c1 is object
c2 = Car()

c2.mil = 8  # changing Instance variable for object c2
print(c1.mil, c1.com, c1.wheels)
print(c2.mil, c2.com, c2.wheels)

Car.wheels = 6  # Changing Class/Static variable will change for all objects
print(c1.mil, c1.com, c1.wheels)
print(c2.mil, c2.com, c2.wheels)
##################################

class Student:
    school = "DnyanPrakash"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):  # This is Instance method, where self is required
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def school_name(cls):  # This is Class method. where cls (ie. class) is required
        return cls.school

    @staticmethod
    def info():  # This is Static method, any random function, which don't need class or object
        return "Random function i.e. addition"


s1 = Student(30, 35, 36)
s2 = Student(85, 76, 70)
print(s1.avg(), s2.avg())  # Calling Instance method
print(Student.school_name())  # Calling Class method
print(Student.info())  # Calling Static method
##########################

# Class within class (inner class)
class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)

    class Laptop:

        def __init__(self):
            self.brand = "HP"
            self.cpu = "Ryzon 5"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Swapnil", 21)
# s1_lap = Student.Laptop()
s2 = Student("Komal", 22)
# s2_lap = Student.Laptop()
# lap1 = s1.lap
# lap2 = s2.lap


s1.show()
# s1_lap.show()
s1.lap.show()
s2.show()
# s2_lap.show()
s2.lap.show()
# lap1.show()
# lap2.show()
########################################

# Class Inheritance
class A:
    def feature1(self):
        print("Feature 1 working!")

    def feature2(self):
        print("Feature 2 working!")


class B:
    def feature3(self):
        print("Feature 3 working!")

    def feature4(self):
        print("Feature 4 working!")


class C(A):  # Class C is child of class A, so inheriting all methods of parent A class; its Single Inheritance.
    def feature5(self):
        print("Feature 5 working!")


class D(C):  # Class D is child of class C and grandchild of class A, so inherits both class's methods; its Multi Level
             # Inheritance.
    def feature6(self):
        print("Feature 6 working!")


class E(A, B):  # Class E is child of two diff classes A & B, so inherits both class's methods; its Multiple Inheritance
    def feature7(self):
        print("Feature 7 working!")

# Creating objects
s1 = A()
s2 = B()
s3 = C()
s4 = D()
s5 = E()

#  Press "Ctrl + Space" after s1. to see features inherited by object
s1.
s2.
s3.
s4.
s5.
########################################

# Constructor / Super in class
class A:
    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Feature1 of A")


class B:
    def __init__(self):
        print("In B init")

    def feature1(self):
        print("Feature1 of B")


class C(A, B):
    def __init__(self):
        super().__init__()  # By default it will call class A's init method
        super(A, self).__init__()  # To call class B's init method
        print("In C init")

    def feature2(self):
        print("Feature2")

    def feat1ofB(self):
        super(A, self).feature1()

# If class do not have __init__ method, it will call it from parent.
# If class has two parents, it will call Left most parent's methods.
# use super(). to call parent's methods from child class
s3 = C()
# Check other method with same name gets called from class A
s3.feature1()
# To print same named method from class B
s3.feat1ofB()
########################################

# Polymorphism i.e. one thing that behaves differently according to environment.
a = 5
b = 6
c = '5'
d = '6'
print(a + b)
print(c + d)
# above lines calls below lines in background
print(int.__add__(a, b))  # __sub__ to subtract, __mul__ to multiply AKA magic methods
print(str.__add__(c, d))


class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1_total = self.m1 + other.m1
        m2_total = self.m2 + other.m2
        s3 = Student(m1_total, m2_total)
        return s3

    def __gt__(self, other):
        slf_total = self.m1 + self.m2
        otr_total = other.m1 + other.m2
        if slf_total > otr_total:
            return True
        else:
            return False

    # def __str__(self):
    #     return "{} {}".format(self.m1, self.m2)  # converting it to string


s1 = Student(30, 45)
s2 = Student(80, 75)

# Lets perform addition of s1 and s2 objects, for this you need to define __add__ method in class.
s3 = s1 + s2
print(s3.m1, s3.m2)

# To compare, add __gt__ method in class.
if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

print(s3)  # If you print it directly, it will print location of object like below and not values of object
# <__main__.Student object at 0x00000204FD866430>
# To avoid getting address and print values instead, add __str__ method in class.
########################################

# Iterator
# lst = [23, 4, 2, 5]
# it = iter(lst)
#
# print(next(it))
# # OR
# print(it.__next__())
#
# # for loop also uses iteration with help of __iter__ and __next__ methods
# for i in lst:
#     print(i)
#
# Lets create class with own iterator
class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


values = TopTen()
print(next(values))
for i in values:
    print(i)
########################################

# Generators / yield  Example: find top ten squares
def top_ten():
    n = 1
    while n <= 10:
        sq = n * n
        n += 1
        yield sq  # yield will keep printing values till loop completes
        # return "{}".format(sq)  # return will skip loop as soon as value got assigned to return


values = top_ten()

for i in values:
    print(i)
########################################

# MultiThreading
# Import
from time import sleep
from threading import *

# Global Variables

# Functions / Class
class Hello(Thread):
    def run(self) -> None:
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self) -> None:
        for i in range(5):
            print("Hi")
            sleep(1)


if __name__ == "__main__":
    try:
        # Main Program
        t1 = Hello()
        t2 = Hi()

        t1.start()  # run method in class will start executing parallel, if we call it using "start()"
        sleep(0.2)
        t2.start()
    except ValueError as e:
        print("Error: Invalid Input!", e)

    except Exception as e:
        print("Error: Something went wrong!", e)

    finally:
        # End Program
        t1.join()  # It will ask main program to wait till t1 completes its job
        t2.join()
        print("End")
########################################

# Binary Search
# Import

# Global Variables
pos = None

# Functions / Class
def bin_div_lst(num, lst):
    lower = 0
    upper = len(lst) - 1
    for __ in range(len(lst)):
        if lower <= upper:
            m = (lower + upper) // 2  # int division i.e 5 // 2 = 2 not 2.5
            if num == lst[m]:
                globals()["pos"] = m
                return True
            else:
                if num < lst[m]:
                    upper = m - 1
                else:
                    lower = m + 1
        else:
            return False


if __name__ == "__main__":
    try:
        # Main Program
        lst = [1, 12, 18, 23, 32, 34, 45, 57, 64, 67, 231, 667, 5567, 7342]  # Binary search only works on sorted list,
        n = 7342                                                             # if you need index position of value.
        if bin_div_lst(n, lst):
            print("Found value {} at {} position".format(n, pos + 1))  # added 1 for human readable position
        else:
            print("Not found {} in list".format(n))

    except ValueError as e:
        print("Error: Invalid Input!", e)

    except Exception as e:
        print("Error: Something went wrong!", e)

#    finally:
        # End Program
########################################
# permutations 
# Python program to print all permutations with
# duplicates allowed


def tostring(lst):
    return ''.join(lst)


# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    if l == r:
        print(tostring(a))
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack


# Driver program to test the above function
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n-1)

# Reverse string
a = "0101"
b = ''.join(reversed(a))
print(a, b)

###################################

# os.chmod("/tmp/test/test1", stat.S_IWOTH)
# current_permissions = stat.S_IMODE(os.stat("/tmp/test/test1").st_mode)
# print(current_permissions)
# print(stat.filemode(current_permissions)[-2])
# if stat.filemode(current_permissions)[-2] == 'w':
#     print("World Writeable file found!")
# os.chmod("/tmp/test/test1", current_permissions-2)
# print(stat.filemode(1023))
# if os.path.exists("/tmp/test/test1"):
#     print("File/dir exists!")
# else:
#     print("File/dir not found!")
# out = "Line"
# with open("/tmp/test/output.csv", "a") as outfile:
#     outfile.write("First,"+out+"\n")
# out = "Row"
# with open("/tmp/test/output.csv", "a") as outfile:
#     outfile.write("Second,"+out+"\n")
# outfile = lambda x: out_file.write(x + "\n")
# try:
#     out_file = open("/tmp/test/out.txt", "a")
#     file = "Test file"
#     print("Hello There" + file)
#     outfile("Hello There " + file)
#     outfile(file + " Hi\n")
#
# except Exception:
#     pass
#
# finally:
#     out_file.close()
# print(stat.filemode(os.stat("/tmp/test/test1").st_mode))
# print(stat.S_IMODE(os.stat("/tmp/test/test1").st_mode))
# print(oct(stat.S_IMODE(os.stat("/tmp/test/test1").st_mode))[2:])
################################################
# filemod file permissions rwx way in python 2
import os
import stat
# curr_perm = oct(stat.S_IMODE(os.stat("/tmp/test/test3").st_mode))[2:]
file = "/tmp/test/test3"
curr_perm = stat.S_IMODE(os.stat(file).st_mode)
# print(oct(curr_perm)[2:])


def filemod(x):
    x = str(oct(x)[2:])
    perm = ['?']
    all_perm = {0: "---", 1: "--x", 2: "-w-", 3: "-wx", 4: "r--", 6: "r-x", 6: "rw-", 7: "rwx"}
    if len(x) == 3:
        for i in x:
            if int(i) in all_perm.keys():
                perm += all_perm.get(int(i))
    else:
        for i in x[1:]:
            if int(i) in all_perm.keys():
                perm += all_perm.get(int(i))
        if x[0] == '1':
            perm[9] = 'T' if int(x[3]) % 2 == 0 else 't'
        if x[0] == '2':
            perm[6] = 'S' if int(x[2]) % 2 == 0 else 's'
        if x[0] == '3':
            perm[9] = 'T' if int(x[3]) % 2 == 0 else 't'
            perm[6] = 'S' if int(x[2]) % 2 == 0 else 's'
        if x[0] == '4':
            perm[3] = 'S' if int(x[1]) % 2 == 0 else 's'
        if x[0] == '5':
            perm[3] = 'S' if int(x[1]) % 2 == 0 else 's'
            perm[9] = 'T' if int(x[3]) % 2 == 0 else 't'
        if x[0] == '6':
            perm[3] = 'S' if int(x[1]) % 2 == 0 else 's'
            perm[6] = 'S' if int(x[2]) % 2 == 0 else 's'
        if x[0] == '7':
            perm[3] = 'S' if int(x[1]) % 2 == 0 else 's'
            perm[6] = 'S' if int(x[2]) % 2 == 0 else 's'
            perm[9] = 'T' if int(x[3]) % 2 == 0 else 't'
    return ''.join(perm)


print(filemod(curr_perm))
##########################################








