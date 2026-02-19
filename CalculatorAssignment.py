import math

# Simple calculator that perform addition, substraction, multiplication, division
# 1. ADD
# 2. SUBTRACTION
# 3. MULTIPLICATION
# 4. DIVISION
# 5. SQUARE ROOT
# 6. EXPONENTIAL

print("select an operation to perform:")
print("1. ADD")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
print("5. SQUARE ROOT")
print("6. EXPONENTIAL")


operation = input()
if operation =="1":
    num1 = input("Enrter first number:")
    num2 = input("Enter second number:")
    #print ("The sum is" + num1 + num2)
    #print ("The sum of two numbers:" + int(num1) + int(num2))
    print ("The sum of two numbers:" + str(int(num1) + int(num2)))

elif operation == "2":
    num1 =input("Enter first number:")
    num2 = input("Enter second number:")
    #print("The sum is" + int(num1) - int(num2))
    print("The Difference is " + str(int(num1) - int(num2)))

elif operation == "3":
    num1 = input("Enter the first number: ")
    num2 = input ("Enter the second number: ")
    print("The Product of two numbers: " + str(int(num1)*(int(num2))))

elif operation == "4":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number")
    print("The division of two number: " + str(int(num1) / int(num2)))

elif operation == "5":
    num = int(input("Enter number: "))
    print("The square root is %f" %(math.sqrt(num)))

elif operation == "6":
    num = int(input("Enter number: "))
    print("The power is %d" %(math.pow(num, 2)) )

else:
    print("Invalid entry")

