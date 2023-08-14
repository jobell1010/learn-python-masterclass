numbers = input("Please enter three integers separated by a comma: ")

list_numbers = numbers.split(",")

for index in range(len(list_numbers)):
    list_numbers[index] = int(list_numbers[index])

print(list_numbers)
print(list_numbers[0] + list_numbers[1] - list_numbers[2])
