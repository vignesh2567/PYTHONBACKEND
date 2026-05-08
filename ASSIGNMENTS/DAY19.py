

# SORTING WITHOUT USING BUILT-IN FUNCTION

numbers = [5, 2, 8, 1, 9,7,11,0]

# Bubble Sort
for i in range(len(numbers)):
    for j in range(len(numbers) - 1 - i):
        if numbers[j] > numbers[j + 1]:
            # swap
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print("Sorted List:", numbers)
