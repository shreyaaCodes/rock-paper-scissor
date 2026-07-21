#VARIABLES = Storage containers for data values 
#python is a dynamically typed language which means you do not have to declare the type of the varriable when you create one.the interpreter infers the type of the varriable baased on the value it is assigned to.
#python is strongly typed language which means that once a varriable is assigned a value of acertain datatype, it cannot be used as a different datatype without explict typecasting.
#We can assign muliple values to multiple varriables in a single line.
#varriables can never start with a numnber .... eg 1name = "shreya" is invalid
#as python is case sensetive language therefore name and Name are two different varriables.
#we can use underscore in varriables instead of space .... eg my_name = "shreya" is valid but my name ="shreya" is invalid .And this is known as snake_case naming convention.
#Keywords are reserved words in python which cannot be used as varriables.
#Same values can be assigned to multiple variables.

name = "Shreya"
age = 21
cgpa =6.4
is_student = True 
print("name:", name)
print("age:", age)
print("cgpa:", cgpa)
print("is_student:", is_student)

print("My name is", name)
print("I am", age, "years old")
print("My cgpa is", cgpa)

fav_language = "Python"
fav_lanuage ="Java"
print(fav_lanuage)

x = 5
y = x
print(y)
