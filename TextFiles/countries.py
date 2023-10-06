input_filename = 'country_info.txt'

countries = {}
with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict
        # countries[code.casefold()] = country_dict

# print(countries)

# while True:
#     choice = input("Please choose a country: ")
#     country_key = choice.casefold()
#     if country_key in countries:
#         chosen = countries[country_key]
#     #     cap = chosen.get("capital", "None")
#     #     print(f"The capital is {cap}")
#         if chosen['capital'] == '':
#             print(f"{choice} does not have a capital city")
#         else:
#             print(f"The capital of {choice} is {chosen['capital']}")
#     elif choice == 'quit':
#         break
#     else:
#         print("I don't know that country")

print("Here is a list of countries with no capital city")
for country, info in countries.items():
    if info['capital'] == "":
        print(country)

print()

print("Fields with blank data")
for country, info in countries.items():
    for key, field in info.items():
        if field == "":
            print(f"{country} has no data for {key}")
