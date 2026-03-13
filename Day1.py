
# Easy Syntax
# Libraries
# Py is Opensource
# Only Interpreter used ? No , compiler is also used

# Why is Py dynamically typed lang ?
#     No need to define Datatype

# math = 40
# pi = 3.14
# name = 'PK'
# print(type(math))
# print(type(pi))
# print(type(name))

# print(2+2)
# print('2'+'2')

# va1 = int(input("Enter frist value: "))
# va2 = int(input("Enter second value: "))

# print(va1+va2)

# print(int(3.14))
# # print(int(10+5j))
#     # Not possible to typecast in Python "Comples no"
# print(int(True))
# print(int(False))
# print(int("4"))

# print(float(3))
# # print(float(10+5j))
#     #  Not possible to typecast in Python "Comples no"
#     # We cant convert complx val to float
# print(float(True))
# print(float(False))
# print(float("4"))

# print(complex(3))
# print(complex(12.8))
# print(complex(True))
# print(complex(False))
# print(complex("5"))
# print(complex("5.6"))

# print(bool(0))
# print(bool(15))
# print(bool(3.14))
# print(bool(0+0j))
# print(bool(False))
# print(bool(0.0))

#1. Write a program for simple intrest
# si = pnr / 100

# pri = 100000
# r = 10
# time = 1

# si = (pri * r * time) / 100
# print(f"Simple intrest: {si}")

#2. wirte  a program to c to f temp

# c = float(input("Enter the temp in C: "))

# f = (c*1.8)+32
# print(f)

#3. Swap
# x = int(input("Enter X: "))
# y = int(input("Enter Y: "))
# x = x + y
# y = x - y
# x = x - y
# print(f"X = {x}") 
# print(f"Y = {y}") 

#4. Height
# h = float(input("Enter height: "))

# inch = h * 12
# cm = inch * 2.54

# print(f"Inch: {inch}")
# print(f"Cm: {cm}")


#5 .reverse

# num = list(input("Enter number: "))
# print(type(num))
# print(num[::-1])

num = input("Enter num: ")
temp = int(num)
l = len(num)
rev = 0

for i in range(l , 0 , -1):
    rem = temp % 10
    temp = temp // 10
    rev += rem * 10**(i-1) 

print(rev)
    
    

