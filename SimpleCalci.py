
# Adding two numbers 
def add(x, y):
   return x + y

# subtract two numbers 
def subtract(x, y):
   return x - y

# multiplies two numbers
def multiply(x, y):
   return x * y

# divides two numbers
def divide(x, y):
   return x / y

print("Choose ")
print("A. Add")
print("B. Subtract")
print("C. Multiply")
print("D. Divide")

# Take input from the user 
choice = input("Select choice(A/B/C/D): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 'A':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == 'B':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == 'C':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == 'D':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")
