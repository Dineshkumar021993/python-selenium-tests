# # print(100+200)
# import keyword
#
# print(keyword.kwlist)
# # print in 1 line
# x = 100.500
# y = 'welcome'
# print(x, y)
# print(type(x), type(y))
#
# # variable declaration in 1 line
# a, b, c = 10, 'welcome dinesh', 1233.5
# print(a, b, c)
# z = a, b, c = 10, 'welcome dinesh', 1233.5
# print(z)
import requests

# # deleting a variable
# a = 100
# b = 'welcome'
#
# del a
# print(a)
# print(b)

# operators
# Arthimatic operators,logical operators,realation

# Arthimatic
# a = 7
# b = 3
#
# print(a + b)  # addition
# print(a - b)  # subtraction
# print(a / b)  # division
# print(a * b)  # multiply
# print(a // b)  # division quotient
# print(a % b)  # division reminder
# print(a ** b)  # exponential

# Relational operators
# < >  >= <= != ==
# a = 10
# b = 20
#
# print(a > b)  # False
# print(a < b)  # True
# print(a >= b)  # False
# print(a <= b)  # True
# print(a != b)  # True
# print(a == b)  # False

# # logical operators
# # and or not
# a = True
# b = False
#
# # a= False
# # b= True
# #
# # a= True
# # b= True
# #
# # a= False
# # b = False
#
# print(a and b)
# print(a or b)
# print(not a)


# concatenation
# a=100
# print("HelloDinesh"+"  "+"WelcomeToPython")
# print("Enter value of a is:",a)
# print(10+10)
# print(10+True) # generally true = 1 and false = 0
# # print(10+"welcome") # invalid statement both 10 and welcome are different datatypes


# # formatting the output
# name, age, salary = "dinesh", 100, 10000.50
# # print(name, age, salary)
# # print("myname is:", name, "my age is:", age, "my salary is:", salary)
# # print("name is:%s age is:%d salary is:%s" % (name, age, salary))
#
#
# # how to take input from user and type conversion
# # generally input takes string that's why int,float
# name = input("Enter your name:")
# age = int(input("Enter ur age:"))
# salary = float(input("Enter ur salary:"))
#
# print(type(name))
# print(type(age))
# print(type(salary))
#
# print(name)
# print(age)
# print(salary)


# IN control statements These are conditional statements(if,if-else,elif)


# age = 15
# if age >= 18:
#     print("elgible for vote")
# else:
#     print("Not eligible for vote")
#
# # elif
# weekend = 5
# if weekend==1:
#     print('sunday')
# elif weekend == 2:
#     print('monday')
# elif weekend == 2:
#     print('tuesday')
# elif weekend == 3:
#     print('thursday')


# looping statements
# for i in range(19):
# also u can use list function
# print(list(range(1, 10, 2)))
# for i in range(1, 10, 2):
#     print("hello Dinesh")
#
# for i in range(10, 1, -1):
#     print(i)
#
# for i in range(-10, -5, 2):
#     print(i)


# looping statements
# while loop
# i = 1
# while i <= 10:
#     print("hello world")
#     i = i + 1
#
# # jumping statements
# # break,continue
# for i in range(1, 10):
#     if i >= 5:
#         break
#     print(i)

# continue
# for i in range(1, 10):
#     if i == 4 or i == 7 or i == 9:
#         # it skips 4,7,8 and continue with remaining values
#         continue
#     print(i)

# numbers and Strings
# some functions
# print(max(12, 15, 56))
# print(min(12, 15, 56))
# # strings
# # all are same while defining strings
# s = "dinesh"
# s1 = 'dinesh'
# s2 = str("dinesh")
#
# print(s)
# print(s1)
# print(s2)
# first started empty string and assigning value after words
# s1 = str()
# s2 = s1.__add__("dinesh")
# print(s2)

# mutable -- can change value of variable once assign
# immutable -- cannot change of variable once assign

# s1 = "welcome"
# s1 = 'dinesh'
# print(s1)

# using * and + with string

# dinesh = "harish"
# dinesh = (dinesh + "Hi")
# print(dinesh)
# print(dinesh*2)

# slicing concept
# str = "dineshkumar"
# print(str[1:7])  # ineshk
# print(str[:6])  # dinesh
# print(str[1:])
# print(str[1:-2])  # ineshkum
#
# # ord and chr function # print ascii and return ascii to normal
# char = ord('A')
# print(char)
#
# number = chr(68)
# print(number)

# max,min,len in strings
# str = "dineshkumar"
# print(max(str))
# print(min(str))
# print(len(str))
#
# # in,not in operators
# a = "dineshkumar"
# print('kumar' in a)
# print('lota' in a)
# print('lota' not in a)

# different methods in string
# s = "welcometodinesh10"
# print(s.isalnum())
# s = "hidinesh"
# print(s.isalpha())
# s = '10000'
# print(s.isdigit())
# s = "for"  # check if given string is reserved keyword
# print(s.isidentifier())
# s = "DINESHKUMAR"  # check the string contains lowercase characters
# print(s.islower())  # false
# print(s.isupper())  # True


# searching for substrings

# s = "Hi dinesh welcome to pYThon"
# print(s.__contains__("welcome"))
# print(s.endswith("python"))
# print(s.startswith("hi"))
# print(s.find("come"))  # returns index position from where it starts
# print(s.find("nesh we"))
# print(s.count("o"))  # no of occurrences of variable
# print(s.capitalize())  # it capitalize first character as a capital letter in string
# print(s.title())  # it capitalize all first characters as capital letter in total string
# print(s.lower()) # it lowers all capital letters
# print(s.upper())
# print(s.swapcase())
# print(s.replace("pYThon" ,"Dinesh"))
# print(s.replace("Th","to"))


# collections
# store multiple sets of data in variable
# list,tuple,dictionary,set
# list -- list is a collection which is ordered and changeable and it is written in [] and it is mutable
# dinesh = ["rajesh", 10, 10.4, "mahesh"]
# print(dinesh)
# dinesh[1] = 100
# print(dinesh)
# dinesh[0] = "Happy"
# print(dinesh)
# mahesh = list()
# # list() is constructor and we can empty list as list() or []
# print(mahesh)
# mahesh1 = []
# print(mahesh1)


# mylist = ["dinesh", "shiva", "shivaleela", "kusuma", "trinad", "baba"]
# mylist[1] = "baburao"
# print(mylist)  # assigning new item in this list
# print(mylist[0])
# print(mylist[1])  # getting required values from the list
#
# # slicing in list collection type
# print(mylist[1:4])

# to get all values in list using loop
# for i in mylist:
#     print(i)
# # check partiular element present in list
# if "apple" in mylist:
#     print("present")
# else:
#     print('not')

# to print no of items in a list
# print(len(mylist))
# Add items to a list
# append will add item at end of list and insert will add iteem whereever u want
# mylist.append("hi")
# print(mylist)
#
# mylist.insert(1, "kivi")
# print(mylist)
#
# # remove item from the list
# mylist.pop(1)
# print(mylist)
# # del item in a list
# del mylist[1]

# clear all items in a list but list will be there but it only delete items in a list
# mylist1 = mylist.clear()
# print(mylist1)

# copy one list to another list # [1, 10, 'dinesh']
# mylist1 = [1,10,"dinesh"]
# mylist2 = list(mylist1)
# print(mylist2)

# list1 = [1,2,3] # [1, 2, 3, 'A', 'B', 'c']
# list2 = ["A","B","c"]
# # list3 = list1 + list2
# # print(list3)
#
# list1.extend(list2)
# print(list1)

# A tuple is ordered but unchangeable and it is immutable and it is declared with ()
# tuple1 = (1,2,3,"dinesh")
# print(tuple1)
# # hre tuple immutable means unchanged so i converted to list and added items
# tuple2=list(tuple1)
# # tuple2[1] = "kanna"
# # print(tuple2)
#
# # accessing tuple elements with slicing
# print(tuple2[2:5])

# tuple1 = ("A","B","C",1,2,3)
# print(tuple1)
# print(tuple1[-4:-1])

# set it is unordered and indexed and mutable, and it is represented with {}
# MySet = {1, 2, 3, "A", "Dinesh", "Suresh"}
# print(len(MySet))
# for i in MySet:
#     print(i)
#
# if "I" in MySet:
#     print("yes")
# else:
#     print("no")
#
# # add single item
# MySet.add("shiva")
# print(MySet)
# # add multiple items into list we use update
# MySet.update("mahesh", "babu", "kusuma", "1")
# print(MySet)
# delete item in a set
# MySet.remove("Dinesh")
# print(MySet)

# Myset = {"dinesh","ganesh","suresh",1,2,3}
# Myset.discard("ganesh")
# print(Myset)

# clear all items from the set
# Myset.clear()
# print(Myset)

# delete total set
# del Myset
# print(Myset)

# joining 2 sets
# MySet1 = {"dinesh","suresh","mahesh"}
# MySet2 = {1,2,3,4}
# # MySet3 = MySet1.union(MySet2)
# # print(MySet3)
#
# # update function is also used to join 2 sets like union
# MySet3 = MySet2.update(MySet1)
# print(MySet3)


# dictionary
# A dictionary is a collection  which is unordered ,changeable and indexed
# dictionary is written in curly braces and it has key value pairs
MyDict = {'name': 'dinesh', 'age': 20, "firstname": "pentakota"}

# print(MyDict['age'])
# print(MyDict['name'])
# print(MyDict)

# changing elements in dictionary
# print(MyDict)
#
# for i in MyDict:
#     print(MyDict[i])

# to get all values in a dictionary using loop
# for i in MyDict.values():
#     print(i)

# print both key value pairs in dictionary
# for i,z in MyDict.items():
#     print(i,z)
# Add item to the dictionary
# MyDict["lastname"] = "Dinesh kumar"
# print(MyDict)

# remove items from the dictionary
# print(MyDict)
# MyDict.pop("age")
# print(MyDict)
# del MyDict["name"]
# print(MyDict)

# print(MyDict)
# delete total dictionary
# del MyDict
# print(MyDict)

# delete only items from the dictionary
# MyDict.clear()
# print(MyDict)


# functions
# function means a set of statements which will perform a task
# 1.function declaration/creation
# 2.function calling
# def helloworld():  # defining the function
#     print("hello dinesh")
#
#
# helloworld()  # calling the function
#
#
# # defining and calling a function with parameter
# def funcwithparameter(name):
#     print("my name is:", name)
#
#
# funcwithparameter("dinesh")
#
#
# def additionof2numbers(a, b):
#     return a + b
#
#
# print(additionof2numbers(2, 3))
# def fun(a, b):
#     return a + b
#
#
# print(fun(10, 20))

# variables
# global and local variables
# the variables create outside of the function called global variables
# the variables create inside of the function  called as local variables
# global_variable = 100  # this is a global variable
# global_variable1 = 200
#
# def func():
#     local_variable = 100  # this is a local variable
#     print(local_variable)
#     print(global_variable)
#     print(global_variable1)
#
#
# func()

# print(local_variable)
# from outside of the function we are unable to access local variable which is declared inside the function

# Actually we can declare global variable in both ways above the function and below the function but indentation should be mandatory

# example
# xyz = 100

# def func():
#     global xyz
#     xyz = 200
#
#     local_xyz = xyz
#
#
#     print(local_xyz)
#
#
# func()


# def fun(a,b)
# we are passing parameters naa like a,b these are 2 types 1.positional parameters 2.keyword parameters

# def dinesh(i, j):
#     print(i, j)
#
#
# dinesh(10, 20)  # positional parameters
# dinesh(j=10, i=20)  # these are key word parameters  because i mention to which variable which value should mention

# example2 in positional and keyword parameters
# def func(i, j=10):
#     print(i, j)
#
#
# func(i=20, j=100)

# def func(a=10,b=100):
#     print(a+b)
# func()


# a = {'a': 10, 'b': 20}
# print(type(a))

# def fun(a,d):
#     print(a**d)
#     print(a+d)
#
# fun(10,5)

# class loginpage:
#     def test_print2numbers(self, a, b):
#         print(a * b)
#         print(a+b)
#         print(a/b)
#
#
# local = loginpage()
# local.test_print2numbers(10, 20)

# class is defined as collection of variables and methods

# a=10
# b=20

# def fun():
#     global a
#     global b
#     x=100
#     y=200
#     print(x+y)
#     print(x*y)
#     print(a+b)
#     print(a-b)
# fun()


# class loginpage:
#     def __init__(self):
#         self.x = 100
#         self.y = 200
#
#     def additionoftwonumbers(self, a, b):
#         # a=10
#         # b=20
#         print(a + b)
#
#     def subtractionoftwonumbers(self, a, b):
#         # a=20
#         # b=30
#         print(a - b)

#     def multiplicationoftwonumbers(self, a, b):
#         # a=10
#         # b=20
#         print(a * b)
#
#     def divisionoftwonumbers(self):
#         # a=20
#         # b=10
#         print(self.x / self.y)
#
#
# login = loginpage()
# login.additionoftwonumbers(10, 20)
# login.subtractionoftwonumbers(10, 20)
# login.multiplicationoftwonumbers(30, 40)
# login.divisionoftwonumbers()


# 2 types of methods we can create
# 1.instance methods --- with object creation we can call
# 2.static methods -- without object creation we can access the variable
# class loginpage:
#     def func(self, a, b):
#         print(a , b)
#
#     @staticmethod
#     def func1(self, a, b):
#         print(a , b)
#
#
# lp = loginpage.func(100,20,30)
# loginpage.func1(100,23,24)

# a, b = 10, 20  # global variables


# class login:
#     a, b = 100, 200  # class variables
#
#     def func(self):
#         a, b = 23, 43  # local variables
#
#         print(a + b)
#         print(self.a + self.b)
#         print(globals()['a'] + globals()['b'])  # to access global variables inside the function we use global keyword


# log = login()
# log.func()
# main advantages of constructor
# if we define variables we need not to create object and call.so we can access any where and in any method throught the class so for this purpose we use constructor
# how to define a constructor
# def __init__(self):
# we no need create a object to access variables in constructor

# class loginpage:
#     def __init__(self):
#         print("this is a constructor")
#
#     def func(self):
#         print("hi i am dinesh")
#
#
# lp = loginpage()  # see here while calling constructor here i did not create any object when call login page constructor called defaultly
# lp.func()

# class Emp:
#     def __init__(self,eid,ename,esal):
#         print(eid,ename,esal)
#
#     def display(self,eid,ename,esal):
#         print(eid,ename,esal)
# emp=Emp(10,"dinesh",1000)

# emp.display(10,"kanna",100000)


# acquiring all the attributes(variables) and behaviour(methods) from one class to another class called inheritance
# reusability and avoid duplication of code

# types of inheritence
# single
# multi level
# hierarchy
# multiple

# single --- from single parent only single child can inherit variables and methods
# multi level --- from 1 parent the child will inherit and another child treat that child as a parent and inherit methods and variables
# class A:
#     def func1(self, a=10, b=20):
#         print(a + b)
#
#
# class B(A):
#     def func2(self, x=10, y=20):
#         print(x + y)
#
# len1 = A()
# # len = B()
# # len.func1()
# # len.func2()
# len1.func1()

# class A:
#     def func1(self, a=10, b=10):
#         print(a + b)
#
#
# class B(A):
#     def func2(self, x=10, y=20):
#         print(x + y)
#
#
# class C(B):
#     def func3(self, p=100, q=200):
#         print(p + q)
#
#
# class D(C):
#     def func4(self, u=12, r=45):
#         print(u + r)
#
#
# len = D()
# len.func1()
# len.func2()
# len.func3()
# len.func4()
#
# len1 = A()
# len1.func1()
#
# len2 = B()
# len2.func1()
# len2.func2()
#
# len3 = C()
# len3.func1()
# len3.func2()
# len3.func3()


# hierarchy Inheritance --- single parent multiple childs
# class A:
#     def func(self, a=10, b=20):
#         print(a + b)
#
#
# class B(A):
#     def func1(self, x=10, y=20):
#         print(x + y)
#
#
# class C(A):
#     p = 100
#     q = 200
#
#     def func2(self):
#         print(self.p * self.q)
#
#
# len = C()
# len.func()
# len.func2()
#
# len1 = B()
# len1.func()
# len1.func1()
#
# len2 = A()
# len2.func()

# multiple inheritence --- 2 parents for 1 single child

# class A:
#     def func(self):
#         a = 10
#         b = 20
#         print(a + b)


# class B:
#     def func1(self):
#         x = 20
#         y = 30
#
#         print(x + y)
#
#
# class C(A, B):
#     def func2(self):
#         p = 100
#         q = 200
#         print(p + q)
#
#
# len = C()
# len.func()
# len.func1()
# len.func2()


# Example2
# class dinesh:
#     a = 10
#     b = 20
#
#     def func(self):
#         print(self.a * self.b)
#
#
# class suresh:
#     x = 20
#     y = 10
#
#     def func1(self):
#         print(self.x - self.y)
#
#
# class mahesh(dinesh, suresh):
#     p = 20
#     q = 30
#
#     def func2(self):
#         print(self.p + self.q)
#
#
# len = mahesh()
# len.func()
# len.func1()
# len.func2()

#
# class dinesh:
#     def func(self, a=10, b=20):
#         print(a + b)
#
#
# class suresh(dinesh):
#     def func(self, x=20, y=10):
#         print(x + y)
#         super().func()
# # when we have two methods in 2 different classes with same name then we use super keyword
# len = suresh()
# len.func()


# modules and packages

# modules ---> collection of functions,classes(variables and methods)
# module means single py file
# if we want to call one module to another module
# we use import or from <module name> import class(or)function name
# Approach1 --- import module name
# Approach2 ---- from module name import class name or function name


# packages
# collection of modules

# import from other packages
# if we want to classes or functions from other modules then use
# import sys
# sys.path.append(package path directory)


# Exception handling
# use try except block
# def func():
#     try:
#         print(x)
#     except:
#         print("leave this exception")
#
# print("hello dinesh")

# locators
# id,class name,tag name,link text,partial linked text,xpath,css selector

# from selenium import webdriver
# from selenium.webdriver.chrome.service import service
# from selenium.webdriver.common.by import By
#
# serv_obj = service(chrome executable<path>)
# driver = webdriver.chrome(service=serv_obj)
# driver.get("www.google.com")


# if we want more elements
# sliders = driver.find_elements(By.class_name,"homeslider-container")
# print(len(sliders))

# if we want to bring text,it is possible only for single text element
# if we want to print text
# followingsibling = driver.find_element(By.class_name,"Xpath")
# print(len(followingsibling))


# application commands
# title
# get
# page_source
# current_url

# print(driver.title)
# print(driver.get)
# print(driver.page_source)
# print(driver.current_url)


# conditional commands
# is_displayed -- it will check particular element is present or not on webpage
# is_enabled -- it will check element is in enabled state or in disabled state,,if element is in enable state then we will get true
# is_selected -- it is escipally for radio buttons and check boxes

# conditional commands
# searchbox = driver.find_element(By.Xpath,"Xpath")
# print(searchbox.is_displayed) //check element is displayed on webpage
# print(searchbox.is_enabled)   //check element is in enabled state or not
# print(searchbox.is_selected)   //check element is in selected or diselected escpially for radio buttons and checkboxes


# radio_button_male = driver.find_element(By.Xpath,"Xpath")
# radio_button_female = driver.find_element(By.Xpath,"Xpath")
# print(radio_button_male.is_selected)
# print(radio_button_female.is_selected)

# browser commands
# driver.close() -- close current browser
# driver.quit() --- close all browsers

# navigational commands
# forward()
# back()
# refresh()

# find_element vs find_elements
# based on xpath if we want to find the single element then we use find_element
# and based on xpath if we want to find multiple webelements then we use find_elements


# print multiple elements in the text
# elements = driver.find_elements(By.Xpath,"Xpath")
# print(len(elements))
# if element in elements
#     print(element.text)


# text vs getattributevalue('value')
# here text method only returns innertext and if inner text is not there it wont return anything
# get value of any attribute if placeholder = 'Dinesh'  ,then we can give get_attribute as placeholder then it returns Dinesh value


# wait commands
# normal wait
# explicit wait
# implicit wait


# for i in range(1,10):
#     print(i)
#
# len(checkboxes)
# if i want to print mutltiple check boxes through loop then we can use
# for i in range(len(checkboxes)):
#     print(checkboxes[i].click)

# if we want to check box is selected state or not by defaultly
# for checkbox in checkboxes:
#     if checkbox.is_selected():
#         print("yes checkbox is in selected state")

# links
# internal link -- link is open in same webpage
# external link -- link is open in some other page
# broken link -- link is implemented in future

# a tag in html dom represents link
# driver.find_element(By.LINK_TEXT,"digital downloads") -- full link text
# driver.find_element(By.PARTIAL_TEXT,"digital") -- partial link text


# HOW TO CHECK BROKEN LINKS IN PAGE
# There is a module called request module in python from this module i will check
# download request module in settings
# import requests as requests
# alllinks = driver.find_elements(By.XPATH,"//a")
# count = 0
#
# for element in alllinks:
#     url = element.get_attribute("href")
#     res = requests.head(url)
#     if res.status_code >= 400:
#         print("link is broken",url)
# count+=1


# select class for dropdown
# element = select(driver.find_element(By.Xpath,"//a"))
# element.select_by_visible_text("india")
# element.select_by_value("10")
# element.select_by_index("10")

# capture all options in dropdown and print them
# alloptions = element.options
# print("total no. of options",len(alloptions))

# for all in alloptions:
#     print(all.text)

# select option from dropdown
# for all in alloptions:
#     if opt.text=="India"
#         opt.click()
#         break

# how to operate alerts
# driver.find_element(By.Xpath,"new").click -- element
# alert_window = driver.switch_to.alert.accept -- enter into alert window and click okk
# driver.find_element(Xpath,"new")


# FRAMES/IFRAMES
# switch_to.frame(name of frame)
# switch_to.frame(id of frame)
# switch_to.frame(webelement)

# switch to window handles
# windowid = switch_to.window(window ID)







