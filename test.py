# def is_leap(year):
#     leap = False
#     if  year%4==0:
#         if year%100==0:
#             if(year%400==0):
#                 leap=True
#             else:
#                 leap=False
#         else:
#             leap=True
#     return leap


# years = [1800, 1900, 2100, 2200, 2300, 2400, 2000, 2012,1]

# for year in years:
#     # year = int(input())
#     print(year, is_leap(year))


# n = int(input())
# print(''.join([str(x) for x in range(1, n+1)]))
# age = 25
# if 18 <= age < 65:
#     print(age)
# x = 'abs'  # rss
# dic = {
#     'a': 'r',
#     'b': 's'
# }
# for x in dic.keys():
#     x.replace(dic.x, dic)

# setA = set()
# englishNewsPaperStudentNumber = int(input('e number : '))
# inputA = input('A item : ').split(' ')
# for i in range(len(inputA)):
#     setA.add(inputA[i])
# setB = set()
# frenshNewsPaperStudentNumber = int(input('f number : '))
# inputB = input('B item : ').split(' ')
# for i in range(len(inputB)):
#     setB.add(inputB[i])
# print(setA)
# print(setB)
# print(setA.difference(setB))
# print(setB.difference(setA))
# print(len(setA.symmetric_difference(setB)))
# print([list(range(100))])

# letters = ['a', 'b', 'c']
# for index, letter in enumerate(letters):
#     print(index, letter)
# try:
#     listA=[1,5,69,3]
#     print(listA.index(0))
#     raise 'no'
# except ValueError:
#     print('Value Error  :  item you are looking found isn\'t founded')
# production=[('production1',10),('production2',152),('production4',0,'96nnbjlngb')]
# production.sort(key=lambda item:item[1])
# print(production)
# people=dict(name='ahmad',id=99622)
# print({name:id for name,id in people.items()})

# ****interview question****
# sentence = "This is a common iterview question"
# letterDict = {}
# for letter in sentence:
#     if letter == ' ':
#         continue
#     else:
#         if letter in letterDict:
#             letterDict[letter] += 1
#         else:
#             letterDict[letter] = 1
# values = sorted(letterDict.items(), key=lambda value: value[1], reverse=True)
# print(values[0])
# def countNumbers(*args) -> int:
#     def counter():
#         sum: int = 0
#         for i in args:
#             sum += i
#         return sum
#     return counter()

# print(countNumbers(1, 2, 3, 6, 98, 6, 85))
# print(type(bool(5)))
# print("""
# welcome to this
# this isn't good
# """)
# _name = 'welcome'
# print(_name)
# m = int(500)
# n = m
# print(type(m))
# print(type(n))
# print(f'm id : {id(m)}\nn id : {id(n)}')
# print(f'm value : {m}\nn value : {n}')
# m = 600
# print(f'm id : {id(m)}\nn id : {id(n)}')
# print(f'm value : {m}\nn value : {n}')


# listA = [1, 7, 4]
# print(id(listA[0]))
# print(id(listA[1]))
# print(id(listA[2]))
# listA.append(77)
# print(id(listA[3]))
# print(id(listA[3]))
# x=f'{5//6}+\'ok\''.upper().split('\'')
# x=round(2.5)
# try:
#     name=input('Enter a name : ')
#     if not name.isalpha():
#         raise TypeError('Enter a vaild name')
# except TypeError as warning:
#     print(warning)
# else:
#     print(f'Welcome back ,{name}')

# name = input('Enter a name : ')
# if not name.isalpha():
#     print('enter a valid name')
# else:
#     print(f'Welcome back, {name}')
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             print(f"__next__ method :\nself.a value : {self.a}, x value : {x}")
#             self.a += 1
#             print(f"self.a value : {self.a}, x value : {x}")
#             return x
#         else:
#             raise StopIteration


# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#     print(x)+++

# # ******************for arpel
# standard_input = 'we are super heros'
# # ******************


# def buildDict(sentence):
#     letter_dict = dict()
#     for letter in sentence:
#         if not letter == " ":
#             if letter in letter_dict:
#                 letter_dict[letter] += 1
#             else:
#                 letter_dict[letter] = 1
#     return letter_dict


# def findOcc(dictionary: dict) -> tuple:
#     new_list = sorted(dictionary.items(), key=lambda kv: kv[1])
#     return list(new_list[len(dictionary)-1]), list(new_list[0])


# user_input = input('Please enter a sentence : ')
# if bool(user_input) and user_input != " ":
#     dictionary = buildDict(user_input)
#     most_occ, less_occ = findOcc(dictionary)

# else:
#     print('Enter a vaild input')
# x=0
# for k in range(10):
#     for i in range(-1,-10,-1):
#         x=x+2
# for i in range(-5, -10):
#     print(i)
# x=[1,3,5,7]
# for item in range(len(x)-1,-1,-1):
#     print(x[item])


# def shift(item, args):
#     new_list = [item]
#     new_list.extend(args)
#     return new_list


# def unshift(args):
#     if(args):
#         return args[1:]


# listA = [1, 6, 39, 34]
# listA = shift(5, listA)
# listB = unshift(listA)
# print(listA)
# print(listB)
# print('hello')
# dic = {'name': 'user', 'id': 8486464}


# def temp(args):
#     dic_item = {}
#     for key, item in args:
#         dic_item[key]=item
#     print(dic_item)


# temp(dic.items())

# import math
# word="Haitham"
# sum=0
# word_len=len(word)
# for letter in word:
#     sum+=ord(letter)
# x=sum
# for i in range(word_len):
#     k=0
#     div=float(f"0.{k}")
#     k=k+1
#     x=math.floor((sum/word_len)*div)
#     sum-=x
#     y=chr(x)
#     print(f"x value : {x}, y value : {y} , letter {word[i]} ord: {ord(word[i])} ")

# listA=[1,2,3,4]
# listB=['a','b','c']
# print([(n,a) for n in listA for a in listB])
# def isItPrime(number):
#     prime_list=[]
#     for i in range(1,number):
#         if number%i!=0:
#             prime_list.append(i)
#     if bool(prime_list):
#         return prime_list
#     else:
#         return "not prime"
# print(isItPrime(75))
# l=lambda x,y :x+y*2
# print(l(1,5))

# class Student:
#     def __init__(self,**kvargs):
#         self.kvargs=kvargs
#     def __repr__(self):
#         return (f"STD-ID : {self.kvargs.get('id')}\nSTD-Name : {self.kvargs.get('name')}")
# std1 = Student(id=9961055569,name='Ahmad Omar')
# std2 = Student(id=5961088569,name='Zain Issa')
# std3 = Student(id=8961054569,name='Sami khalid')
# std_group=[std1,std2,std3]
# def f1(a):
#     print('F1 was called!',a)
#     return 'F1 gift $8800'
# def f2(func,a=5):
#     print('F2 was called')
#     value=func(a)
#     print('F2 was ran')
#     return value

# print(f2(f1))

# def getName(*args, **kwargs):
#     msg="No content have been passed"
#     print("Values from getName Function : ",args," , ",kwargs)
#     if args and kwargs:
#         return f"{args}, {kwargs}"
#     elif args:
#         return args
#     elif kwargs:
#         return kwargs
#     else:
#         return msg


# def printData(func, *args, **kwargs):
#     if func:
#         return func(*args,**kwargs)
#     else:
#         return "No function has been passed"


# print(printData(getName,'Haitham','Omar',id=978933255))
# print(printData(getName,'Haitham','Omar'))

# def document(func):#getTitle('erlcome')
#     def decorateTitle(title):
#         print('*'*20)
#         func(title)
#         print('*'*20)
#     return decorateTitle


# @document
# def getTitle(title):
#     print(f"{title}")


# getTitle('Welcome')
# listA=[1,7,9,3,5,86,9,3,9,3,6]
# def funA(element):
#     if element>10:
#         return element
# import queue as q
# lineA = q.Queue([1, 3, 6, 9, 3])
# print(lineA)
# type_of=lambda x:type(x)
# print(type_of(7))
# print(type_of('w'))
# print(type_of(False))
# class x:
#     def __init__(self,x):
#         self.x=x
# x = x(5)

# import os
# from datetime import datetime
# os.chdir('/home/dev/Desktop')
# os.makedirs('test')
# os.chdir('/home/dev/Desktop/test')
# print(os.getcwd())
# os.chdir('/home/dev/Desktop/test')
# for i in range(10):
#     os.mkdir(f'folder n{i}')
# for i in range(10):
#     os.rename(f'folder n{i}', f'python_folder{i}')
# for i in range(10):
#     print(os.stat(f'python_folder{i}'))
#     human_readable_date=os.stat(f'python_folder{i}').st_mtime
#     print(f'python_folder{i} st time : {datetime.fromtimestamp(human_readable_date)}')
# os.chdir('/home/dev/Desktop/test')
# os.mkdir('file')
import datetime
from typing import cast
# import pytz
# bday = datetime.date(1996, 8, 25)
# today = datetime.date.today()
# age = today-bday
# print(age.year)
# for tz in pytz.all_timezones:
#     print(tz)
# bday='May 5, 1990'
# print(datetime.datetime.strptime(bday,'%B %d, %Y'))
# import os
# execute_counter = None


# def readFile(fileName):
#     global execute_counter
#     my_file = f'{fileName}.hmg'
#     os.chdir('/home/dev/Desktop/test')
#     base = os.path.splitext(my_file)[0]
#     os.rename(my_file, base + '.txt')
#     with open(f'{fileName}.txt', 'r') as test_txt:
#         execute_counter = int(test_txt.read())
#         print(f'This code has been compiled :{execute_counter}')
#     base = os.path.splitext(my_file)[0]
#     my_file = f'{fileName}.txt'
#     os.rename(my_file, base + '.hmg')


# def writeOnFile(fileName):
#     global execute_counter
#     my_file = f'{fileName}.hmg'
#     os.chdir('/home/dev/Desktop/test')
#     base = os.path.splitext(my_file)[0]
#     os.rename(my_file, base + '.txt')
#     with open(f'{fileName}.txt', 'w') as test_txt:
#         test_txt.write(str(execute_counter+1))
#     base = os.path.splitext(my_file)[0]
#     my_file = f'{fileName}.txt'
#     os.rename(my_file, base + '.hmg')


# readFile('test')
# writeOnFile('test')
# Generators
# def squareNum(nums):
#     for i in nums:
#         yield i


# nums = squareNum([1, 2, 3, 6, 9, 3, 45])
# print([num for num in nums])
# class Employee:
#     # class variable definition
#     raise_salary = 2.5

#     def __init__(self, first, last, pay) -> None:
#         self.first = first
#         self.last = last
#         self.pay = pay

#     def getFullName(self):
#         return f"First name : {self.first}, last name : {self.last}"

#     @staticmethod
#     def printGreeting():
#         print('Welcome')


# class Developer(Employee):

#     def __init__(self, first, last, pay, prog_lang) -> None:
#         self.prog_lang = prog_lang
#         super().__init__(first, last, pay)


# e1 = Employee(first='haitham', last='Mughrabi', pay=25800)
# e1 = Developer(first='haitham', last='Mughrabi', pay=25800,prog_lang='python')
# print(e1.getFullName())
# e1.printGreeting()
# dic={
#     'x':4,
#     'y':30
# }
# dic2={
#     'x':12,
#     'y':12
# }
# for key, value in dic.items():
#     if dic.get(key)==dic2.get(key):
#         print('dic.get(key)==dic2.get(key)')
#     elif dic.get(key)>=dic2.get(key):
#         print('dic.get(key)>=dic2.get(key)')
#     elif dic.get(key)<=dic2.get(key):
#         print('dic.get(key)<=dic2.get(key)')
#     else:
#         print('operation hasn\'t completed')

# elif self.__dimintions.get(key) >= other.__dimintions.get(key):
#             print('dic.get(key)>=dic2.get(key)')
#         elif self.__dimintions.get(key) <= other.__dimintions.get(key):
#             print('dic.get(key)<=dic2.get(key)')
#         else:
#             print('operation hasn\'t completed')
# class TagCloud:

#     def __init__(self, price) -> None:
#         self.__tags = {}
#         self.__set_price(price)

#     def add(self, tag):
#         self.__tags[tag] = self.__tags.get(tag, 0)+1

#     def __iter__(self):
#         return iter(self.__tags)

#     def __set_price(self, price):
#         self.__price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, val):
#         self.__set_price(val)

#     @price.deleter
#     def price(self):
#         del  self.__price
#         print('deleted')


# t1 = TagCloud(12)
# print(t1.price)
# t1.price = 30
# print(t1.price)
# del t1.price
# print(t1.price)
# t1.add('user')
# t1.add('f')
# t1.add('fdser')
# t1.add('uservfvcv')
# t1.add('useeer')
# for t in t1:
#     print(t)
# from abc import ABC, abstractmethod

# class Father (ABC):
#     @abstractmethod
#     def tall(self):
#         pass

# class Son(Father):
#     def tall(self):
#         print('tall')
# def fs(father_son):
#     father_son.tall()
# h=Son()
# fs(h)