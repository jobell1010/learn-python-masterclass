panagram = """The quick brown
 fox jumps\tover
  the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,887"

list_numbers = numbers.split(",")
print(list_numbers)

# new_list = []
# for item in list_numbers:
#     new_list.append(int(item))
#
# print(new_list)

for index in range(len(list_numbers)):
    list_numbers[index] = int(list_numbers[index])

print(list_numbers)
