# 8 random integers between 1–100
numbers = [23, 78, 5, 91, 34, 67, 12, 49]  

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Numbers:", numbers)
print("Biggest number:", largest)
print("Smallest number:", smallest)
