import csv

input_filename = 'country_info.txt'

dialect = csv.excel
dialect.delimiter = '|'

countries = {}

with open(input_filename, encoding='utf-8', newline='') as countries_file:
    # get the column headings from the first in eof the file
    headings = countries_file.readline().strip('\n').split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()
    reader = csv.DictReader(countries_file, dialect=dialect, fieldnames=headings)
    for row in reader:
        countries[row['country'].casefold()] = row

while True:
    choice = input("Please choose a country: ")
    country_key = choice.casefold()
    if country_key in countries:
        chosen = countries[country_key]
    #     cap = chosen.get("capital", "None")
    #     print(f"The capital is {cap}")
        if chosen['capital'] == '':
            print(f"{choice} does not have a capital city")
        else:
            print(f"The capital of {choice} is {chosen['capital']}")
    elif choice == 'quit':
        break
    else:
        print("I don't know that country")
