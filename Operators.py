#OPERATORS = Operators are special symbols that are used to perform operations on variables and values. Python provides different types of operators such as Arithmetic, Assignment, Comparison, Logical, Membership, and Identity operators.
# 1. Arithimetic operators = These operators are used to perform mathematical operations like addition , substraction , multiplication , division , floor division , modulus ,  exponents .
# a) Addition :- This operator is used to add two numbers . 
#eg....
# a = 4 
# b = 10 
# print(a+b)
# a = "21"
# b = "42"
# print(a+b)  #Yahan ADDITION nhi hua  This is known as CONCATINATION  in which we are joing two strings to form one string.We never add strings and integers because it will give an error.

# b) Substraction Operator (-) :- This operator is used to subtract two numbers.
#eg....
# a = 10 
# b = 4
# print(a-b) 

# c) Multiplication Operator (*) :-This operator is used to multiply two numbers.
#eg....
# a = 10 
# b = 5
# print(a*b) 
#but if we multiply two strings then it will repeat the string for the number of the times we multiply it with.
#eg...
# a = "Hello" 
# b = 3 
# print(a*b)  #output = HelloHelloHello

# d) Division Operator (/) :- This operator is used to diivde two numbers and it will give the output in float value.
#eg....
# a = 10 
# b = 2
# print(a/b)

# e) Floor Division Operator (//) :- This operator is used to divide two numbers and it will give the output in integer value.
#eg....
# a =10
# b = 3
# print(a//b)

# f) Modulus Operator(%) :- This operator is used to find the remainder of the division of the two numbers. It will give the output in integer value . It is used to check whether the number is odd or even , if the output is ZERO then the number is even and if the output is ONE then the number is odd.
#eg...
# a = 10 
# b = 7
# print(a%b)

# g) Exponent Operator (**) :- This operator is used to find the power of the number. It will give the output in integer value. 
#eg....
# a = 2 
# b= 5 
# print(a**b)
# print(9/2)
# print(9//2) 
# print(9%2)  
# print(3**3)

# 2. ASSIGNMENT OPERATOR :- These operators are used to assign values to the variables.
# a) Assignment Operator (=) :- This operator is used to assign the value to the varriable.
#eg....
# x = 10 
# print(x)

#b) Addition Assignment Operator(+=) :- This operator is used to add the value to the varriable and store the new value in the same variable. 
# eg....
# number = 10 
# number+= 5
# print(number) 
# name = "Shreya"
# name +="Singh"
# print(name) # This is known as CONCATINATION in which we are joing two strings to form one string

#c) Subtraction Assignment Operator(-=) :- This operator is used to subtract the value from the varriable and store the new value in the same varriable .
#eg....
# sallary = 50000
# sallary-= 5000 
# print(sallary)

#d) Multiplication Assignment Operator(*=):- This operator is used to multiply the value with the varriable and store the new value in the same varriable.
#eg....
# x = 8
# x*=2
# print(x)
# text = "Hello"
# text *= 3
# print(text)  #This is known as CONCATINATION  in which we are joining two strings to form one string.

#e) Division Assignment Operator(/=) :- This operator is used to divide the value with the varriable and store them in the same varriable. It will give the output in the float value.
#eg....  
# x = 10
# x/=2
# print(x)

#f) Floor Division Assignment Operator(//=) :- This operator is used to divide the value with the varriable and store the new value in the same varriable. It will give the output in the integer value. 
#eg....  
# x = 10
# x//=3
# print(x)

#g) Modulus Assignment Operator(%=) :- This operator is used to find the remainder of the division of the two numbers and store the new value in the same varriable. It will give the output in the integer value.It is used to check whether the number is odd or even, if the number is even then the output is zero and if the number is odd then the output is one.
#eg.... 
# x = 10 
# x%=3
# print(x)

#h) Exponent Assignment Operator(**=) :- This operator is used to find the power of the number and store the new value in the same varriable. It will give the output in the integer value.
#eg....
# x =4
# x**=3
# print(x)

# x = 10
# x+= 5
# x*=3 
# x-=9
# print(x)

# x = 10
# y= x
# x = 20 
# print(y) #OUTPUT is 10 because y is assigned the value of x before x is changed to 20. Therefore, y retains the originated value of x which is 10.

#Multiple Assignment :- In python we can assign mmultiple values to multiple variables in a single line.
# a, b, c = 10, 20, 30
# print(a)
# print(b)
# print(c)
 
#Variable Swapping (without third variable) :- In python we can swap the values of two variables in a single line.Exchamging of values of two variables 
# a = 10
# b = 20 
# a, b = b, a
# print(a)
# print(b)

# a = 10 
# b = 20
# temp = a 
# a = b
# b = temp 
# print(a)
# print(b)

# 3. Comparision Operator :- This operator is used to compare two values or expressions .  The result of a comparision is always a Boolean value either TRUE or FALSE.
#We use comparision operator to check wheather the two values are equal or not , greater thann or less than the other value. 
# age = 18
# print(age>=18)

#There are 6 comparision operator in python:-----
# a) Equal to (==) :- This operator is used to check whether the two values are equal or not. If the two values are equal then it will return TRUE otherwise it will return FALSE.
#eg....
# x = 10
# print(x==10)
# b) Not Equal To (!=) :- This opearator is used to check whether the two values are different.
#eg....
# print(10!=5)

# c) Greater Than(>) :-  This operator is used to check whether the left value is greater than the right value. If the left value is greater than the right value then it will return TRUE otherwise it will return FALSE.
#eg.....
# print(20>45)

# d) Less Than (<) :- This operator is used to check whether the left value is less than the right value. if the left value is less than the right value then it will return TRUE otherwiswe it will return FALSE.
#eg......
# print(20<45)

# e) Greater Than or Equal To (>=) :- This operator is used to check whether the left value is greater than or equal to the right value. If the left value is greater than or equal to the right value then it will give TRUE otherwise it will return FALSE.
#eg....
# print(18>=18)

# f) Less Than or Equal To (<=) :- This operator is used to check whether the left value is less than or equal to the right value.
#eg....
# print(23<=23)

#Comparision Between Strings :-In python we can also compare two strings using comparision operators. the comparision between two strings is done on the basis of the ASCII value of the characters in the string. The ASCII value of the character is a unique number assigned to each character.The string with higher ASCII value is considered greater than the string with lower ASCII value. The comparision between two strings is done character by character from lwft to right. The first character of the string is compared first, if they are equal then the second character is compared and so on. If all the characters are equal then the strings are considered equal. If one string is a prefix of the other string then the shorter string is considered less than the longer string.
#eg....
# print("apple" == "apple")
# print("apple" != "banana")
# print("apple" < "banana")
# print("apple" > "banana")

#Chained Comparision :- In python we can also compare more than two values using comparision operators. The comparision is done from left to right. The first two values are compared first, if they are equal then the second and third values are compared and so on. If all the values are equal then the result is TRUE otherwise it is FALSE.
#eg....
# x = 7
# print(5<x<10)

#Operator Precedence :- In python we can use multiple operators in a single expression. The order in which the operators are evaluated is known as operator precedence. The operator with higher precedence is evaluated first. The operator with lower precedence is evaluated later. If two operators have the same precedence then they are evaluated from left to right.    
#eg....
# print(10+5>12)


# 4. Logical Operators :- These operators are used to combine multiple conditions and return a single Boolean value. The logical operators are AND, OR, and NOT
# a) AND Operator (and) :- This operator is used to check whether both the conditions are TRUE or not. If both the conditions are TRUE then it will return TRUE otherwise it will return FALSE.
#eg....
# print(True and False)

# b) OR Operator (or) :- This operator is used to check whether at least one of the conditions is TRUE or not. If at least one of the conditions is TRUE then it will return TRUE otherwise it will return FALSE.
#eg....
# print(True or False)

# c) NOT Operator (not) :- This operator is used to reverse the Boolean value of the condition. If the condition is TRUE then it will return FALSE and if the condition is FALSE then it will return TRUE.
#eg.... 
# print(not True)

# Short Circuit Evaluation :- In python we can use short circuit evaluation to optimize the performance of the logical operators. In short circuit evaluation, the second condition is not evaluated if the first condition is sufficient to determine the result. For example, in the AND operator, if the first condition is FALSE then the second condition is not evaluated because the result will be FALSE anyway. Similarly, in the OR operator, if the first condition is TRUE then the second condition is not evaluated because the result will be TRUE anyway.
#eg....
# print(5 > 3 and 10 < 20)

# 5. Identity Operators :- These operators are used to check whether two variables are referring to the same object in memory or not. The identity operators are is and is not.
# a) is Operator :- This operator is used to check whether two variables are referring to the same object in memory or not. If both the variables are referring to the same object in memory then it will return TRUE otherwise it will return FALSE.
#eg....
# x = [1,2,3]
# y = x  
# print(x is y)

# x = [1,4]
# y = [1,4]
# print(x is y)

# b) is not Operator :- This operator is used to check whether two variables refers to different objects in the memory .
#eg....
# x = [1,2]
# y = [1,2]
# print(x is not y)

# x = 10
# y = x
# print(x is not y)
 
# is None :- It checks object identity and it is the recomemended way in Python. 

# 6. Membership Operator :- This operator is used to check whether a value is present in a sequence or collection. They always return a boolean value .
# there are two types of membership operator in and not in 
# a) in Operator :- This operator checks whether a value exists in a sequence or collection.
#eg.....
# in Operator with STRING 
# name = "Python"
# print("P" in name )
# print("A" in name)
# text = ("Hello World")
# print("" in text) TRUE because SPACE is also a string character.


# with LISTS
# numbers = [1,34,45]
#print(34 in numbers)
# print(46 in numbers)

#with TUPLE
# t = (32,45,65)
# print(32 in t)
# print(87 in t)

#with DICTONARY
# student = {
#     "name":"shreya",
#         "age" :21
#            }
# print("name" in student)
# print("shreya" in student) #FALSE because with dictonay in operator always check for keys . It is by default .
# # If you want to check values so
# print("shreya" in student.values())

# b) not in Operator :- This operator checks whether a value does not exist in a sequence or collection . 
#eg.....
# numbers = [10, 20, 30]
# print(40 not in numbers)
# print(20 not in numbers)

#WHOLE WORD CHECK
# text = ("I love Python")
# print("Python" in text)
# print("java" in text)

#with NUMBERS 
# print(2 in 12456) ERROR because integer is not iterable so membership operatror does not work with integers.

#OPERATOR PRECEDENCE
# print(not("A" in "APPLE"))

# Decision Making :- The process of excuting different blocks of code based on a condition.
#if Statement :- The if statement is used to excute a block of code only a given condition is TRUE.
#SYNTAX:-
#if condition:
    #statement -- if we forgot to use colon it will give syntax error

#Indentation :- Giving spaces in the starting of code is known as indentation . Indentation is important because it defines the block of code that belongs to the if statement. Without proper indentation, Python raises an indentation Error

# if True:
#     print("Python")  
# if False:
#     print("Hello")  

# age = 20

# if age >= 18:
#     print("Adult")

# marks = 30

# if marks >= 40:
#     print("Pass")

# x = 10

# if x == 10:
#     print("A")
    
    
# print("B")

# Multiple Statements Inside if :-All the lines of code are excuted which are the under same indentation if the conditiomn is true.\
# age = 20 

# if age>= 18:
#     print("You are eligible to vote.")
#     print("You can apply for a driving.")
#     print("You are an adult.")
    
# print("Program Ended")

# age = 15    

# if age>= 18:
#       print("You are eligible to vote.")
#       print("You can apply for a driving.")
#       print("You are an adult.")
    
# print("Program Ended")    Agar condition false hai to if ke andr ki teeno lines skip ho jayengi sirf if ke bahar wali line hi print hogi.


# if True:
#     print("A")
#     print("B")
    
# print("C")  

# if False:
#     print("Python")
#     print("Java")
    
# print("C++")  

# x = 5

# if x > 2:
#     print("One")
    
# print("Two")

# print("Three")       