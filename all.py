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









