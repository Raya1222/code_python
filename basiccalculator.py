# program goal is to build a program that can add, subtract, multiply, and divide two numbers

#functional decompostion:
#1. obtain a way to grab 2 numbers 
#2. obtain a way to choose add,multiply,or divide
#3. do the wanted calculations with the given two number
#4.output the calculation results 

print("welcome to our calculator app!")
#1:
num1 = int (input("enter the first number:"))
num2 = int (input("enter the second number:"))

#2.
choice = input("choose either, add, subtract, multiply, or divide: ")

#3/#4
if choice == "add":
    print(num1+num2)
elif choice == "subtract":
    print(num1-num2)
elif choice == "multiply":
    print(num1*num2)
elif choice == "divide":
    print(num1/num2)
