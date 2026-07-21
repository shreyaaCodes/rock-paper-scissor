#The conversion of one datatype to another datatype is known as typecasting 
first_number = input("Enter the first_number:")
second_number = input("Enter the second_number:")
print("The sum of twonumbers is:" , (first_number)+(second_number))

#There are two types of typecasting
#implicit typecasting  = pyhton automatically converts one datatype to another datatpe

x = 10 
y = 12.4 
print(x+y)# This is implicit typecasting because python automatically converts the integer datatpe into float datatype and then adds the two numbers and gives the output as float datatype
#python converts the lower datatype to higher datatype automatically to prevent data loss and to give correct output.In this case python converts the integer datatype to float datatype because float is higher datatype than integer datatype and then adds the two numbers and gives the output as float datatype .

#Explicit typecasting = When the user manually converts one datatype to another datatype is known as expliicit typecasting 

age = int(input("Enter your age:"))
print("my age is", age)# This is explict typecating because the user manually converts the input string datatype to integer datatype using int() function and then prints the output as integer datatype 

x = int("34")
print(type(x))

print(bool(0))#zero = FALSE negative number = TRUE positive number = TRUE

name =(input("Enter your name:"))
age = (int(input("Enter your age:")))
height = (float(input("Enter your height:")))
is_student = (bool(input("Are you a student? (True/False):")))
cgpa = (float(input("Enter your cgpa:")))
college = (str(input("Enter your college:")))
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(cgpa))
print(type(college))