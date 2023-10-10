import csv

input_filename = 'country_info.txt'

countries = {}

with open(input_filename, encoding='utf-8', newline='') as countries_file:
    reader = csv.DictReader(countries_file, delimiter='|')
    for row in reader:
        countries[row['Country'].casefold()] = row

while True:
    choice = input("Please choose a country: ")
    country_key = choice.casefold()
    if country_key in countries:
        chosen = countries[country_key]
    #     cap = chosen.get("capital", "None")
    #     print(f"The capital is {cap}")
        if chosen['Capital'] == '':
            print(f"{choice} does not have a capital city")
        else:
            print(f"The capital of {choice} is {chosen['Capital']}")
    elif choice == 'quit':
        break
    else:
        print("I don't know that country")
