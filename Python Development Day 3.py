# Python For-While Loops

# i=0
# while i<10:
#     i+=1
#     if i==11:
#         break
#     print(i)

# i=0
# while i<100:
#     i+=1
#     if i==101:
#         break
#     print(i)

# i=0
# while i<100:
#     i+=3
#     if i>90:
#         break
#     print(i)

# Python Functions

# def my_function():
#     print("Call new fn")
# my_function()
#
# def my_function1():
#     print("Call new fn1")
# my_function1()
#
# def test_function():
#     print("Print test fn")
# test_function()

# Arguments /Calling functions

# def my_functions(fname):
#     print(fname +" "+ "qwerty")
#
# my_functions("Email")
# my_functions("Name")
# my_functions("Class")

# a=20
# b=90
# if a+b==110:
#        # print("Case Passed")
# # print("Case failed")
#  def logical_function():
#     print("test")
# logical_function()
#
# x=90
# y=88
# if x+y==178:
#     logical_function()
# Taking user inputs using functions

# def my_function():
#     print(int(input("Enter Your Age")))
# a=(int(input("Enter a number")))
# b=(int(input("Enter another number")))
# if a+b>0:
#     z=print(int(input("Enter your Age")))
#     if z!=0:
#         print("Welcome to the website")
#         print("Lorem ipsum")
#     else:
#         print("SORRY")
# if a+b>0: and


# if input==int:
#     def my_function():
# print("Yes")
# my_function()

#     print("HAHAHA")
# if input==Yes:

# Simple Calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:

    # Taking user inputs
    choice =input("Enter Your Choice 1/2/3/4:")

    if choice in ('1','2','3','4'):
            num1=float(input("Enter first number"))
            num2=float(input("Enter second number"))
    else:
        print("Please enter from the given choices")
    if choice=='1':
            print(num1, "+", num2, "=", add(num1, num2))
    elif choice=='2':
            print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice=='3':
            print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice=='3':
            print(num1, "/", num2, "=", divide(num1, num2))













