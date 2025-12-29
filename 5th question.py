# Ask user for two numbers (as strings)
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Convert strings to integers
a = int(num1)
b = int(num2)

# Calculations
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

# Compare which one is bigger
if a > b:
    print("First number is bigger")
elif b > a:
    print("Second number is bigger")
else:
    print("Both numbers are equal")
