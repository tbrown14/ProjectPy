from array import *
import math
import datetime

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

#Fibonacci Sequence 

# a,b = 0,1
# for i in range(0,10):
#     print(a)
#     a,b = b, a + b

#Dictionary 

# my_dict = {'name': 'Bronx', 'age': '22', 'WorkType': 'Programmer'}
#     for key,val in my_dict.items():
#         print("my {} is {}".format(key,val))

# tax = 0.13
# price = input()

# def calc(price, tax):
    
#     calcTax = float(price) * tax
#     total = calcTax + float(price)
#     return total
    

# answer = calc(price, tax)
# print(answer)


# def monkey_trouble(a_smile, b_smile):
#   if a_smile and b_smile:
#     return True
#   if not a_smile and not b_smile:
#     return True
#   return False


# def sum_double(a, b):
#   sum = a + b
  
#   if a ==b:
#     sum = sum *2
#   return sum

# name = 'Travis'
# age = 22
# print("hello " + name + " your are " + str(age))

# print("my name is {name} and i am {age}".format(name=name,age=age))

# fruit = ['apple', 'banana', 'grapes', 'orange']

# print (fruit[1])
# print(len(fruit))

# fruit.append('mango')

# print(fruit)

# person = {
#     'first_name': 'john',
#     'last_name': 'brown',
#     'age': 22
# }

# print(person.get('last_name'))

# #add key vale

# person['phone'] = '807-333-2323'

# print(person.items())
# person2 = person.copy()
# person2['country'] = 'Canada'

# print(person2)


# def sayHello(name):
#     print("hello " + name)

# sayHello('Travis')

# def getSum(num1,num2):
#     total = num1 + num2
#     return total

# print (getSum(10,2))

# getSum = lambda num1, num2: num1 + num2

# print(getSum(10,3))

# x = 10 
# y = 11 

# if x>y:
#     print("x is greater than y")


# if x>y:
#     print("x is greater than y")
# elif x == y:
#     print("x is equal to y")
# else:
#     print("x is greater than y")



# if x > 2 and x <= 10:
#     print("x is greater than 2 and less than or equal to 10 ")


# if x > 2 or x <= 10:
#     print("x is greater than 2 and less than or equal to 10 ")

# if not(x == y):
#     print("x is not equal to y")

# x = 13 
# numers = [1,2,3,4,5]
# # in 
# if x in numers:
#     print(x in numers)

# #not in 
# if x not in numers:
#     print(x in numers)

people = ['john', 'travis', 'sam', 'todd']

# for x in people:
#     print(x)

# for x in people:
#     if x == 'sam':
#         break
#     print(x)

# for x in people:
#     if x == 'sam':
#         continue
#     print(x)

# for i in range(len(people)):
#     print(people[i])

# for i in range(0,11):
#     print(i)

# count = 0 

# while count <=10:
#     print(count)
#     count += 1

# today = datetime.date.today()
# print(today)

#class
# class User:
#     #constructor
#     def __init__(self, name, email , age):
#         self.name = name
#         self.email = email
#         self.age = age

#     def greeting(self):
#         return f'my name is {self.name} i am {self.age}'
        
#     def has_birthday(self):
#         self.age +=1



# #extends class
# class Customer(User):
#      def __init__(self, name, email , age):
#         self.name = name
#         self.email = email
#         self.age = age
#         self.balance = 0
        
#      def set_balance(self, balance):
#         self.balance = balance

#      def greeting(self):
#         return f'my name is {self.name} i am {self.age} and my balance is {self.balance}'

        

# #initial user obj
# travis = User('travis brown', 'email@gmail.com', 22)

# #init customer 
# janet = Customer('janet jone', 'Janet@yahoo.com', 25)
# janet.set_balance(500)
# print(janet.greeting())

# travis.has_birthday()
# print(travis.greeting())
