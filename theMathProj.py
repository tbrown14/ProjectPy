from array import *
import math

# num1 = input('Enter your first number ')
# num2 = input('Enter your second number ')
 
# def math_Func(num1,num2):
#   result = int(num1) + int(num2)
#   return result

# ans = math_Func(num1,num2)

# print(ans)

# #Comment Test


# x = input('Enter your first number ')
# y = input('Enter your second number ')

# if(x>y):
#     print('X is greater than y')
# elif (x<y):
#         print('Y is greater than x')

        #test

        #Change
    
    #something

# l=[]
# for i in range(2000, 3201):
#   if(i%7==0) and (i%5!=0):
#     l.append(str(i))

# print(','.join(l))

# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)

# x=int(input())
# print (fact(x))

# n=int(input())
# d=dict()
# for i in range(1,n+1):
#   d[i]=i*i
# print (d)

# enteredValues = input()
# l =enteredValues.split(',')
# t=tuple(l)
# print(l)
# print(t)




# class GetInputClass(object):
#   def __init__(self):
#     self.s = ""

#   def getString(self):
#       self.s = input()

#   def printString(self):
#       print(self.s.upper())

# strObj = GetInputClass()
# strObj.getString()
# strObj.printString()


# c=50
# h=30

# value = []
# items=[x for x in input().split(',')]

# for d in items:
#   value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
#   print(','.join(value))

# value1 = input()


# twoDArray = [int(x) for x in value1.split(',')]
# rowNumber = twoDArray[0]
# colNumber = twoDArray[1]
# multilist = [[0 for col in range (colNumber)] for row in range(rowNumber)]

# for row in range(rowNumber):
#   for col in range(colNumber):
#     multilist[row][col]= row*col

# print(multilist)

# s = input()
# words = [word for word in s.split(" ")]
# print (" ".join(sorted(list(set(words)))))

# value = []
# items=[x for x in input().split(',')]
# for p in items:
#     intp = int(p, 2)
#     if not intp%5:
#         value.append(p)

# print (','.join(value))       

#Check if a nuber in the range 1-101 is divisable by 5 and 3 
#FIZZ BUZZ 
# for num in range(1,101):
#     if num % 5 == 0 and num % 3 == 0:
#         print("FIZZBUZZ")
#     elif num % 3 == 0:
#         print("FIZZ")
#     elif num % 5:
#         print("BUZZ")
#     else:
#         print (num)

# #Fibonacci Sequence 

# a,b = 0,1
# for i in range(0,10):
#     print(a)
#     a,b = b, a + b

#Dictionary 

# my_dict = {'name': 'Bronx', 'age': '22', 'WorkType': 'Programmer'}
#     for key,val in my_dict.items():
#         print("my {} is {}".format(key,val))

tax = 0.13
price = input()

def calc(price, tax):
    
    calcTax = float(price) * tax
    total = calcTax + float(price)
    return total
    

answer = calc(price, tax)
print(answer)