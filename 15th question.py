# give list
numbers = [12, 45, 3, 98, 7, 34, 21]

count = 0

for num in numbers:
    # a) print each number
    print(num)

    # b) print only numbers greater than 30
    if num > 30:
        print("Greater than 30:", num)
        count += 1

# c) count how many numbers are greater than 30
print("\nCount of numbers greater than 30:", count)
