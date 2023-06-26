available_option = "12345"

menu = "Here are the following options\n"\
       "1. Banana\n" \
       "2. Large hat\n"\
       "3. Eleven small dogs\n"\
       "4. Dinner\n"\
       "5. Brilliant\n"\
       "0. Exit"

print(menu)

chosen = ""
while chosen != "0":
    chosen = input("Please choose from the available options?")

    if chosen in available_option:
        print("You have chosen option {}! Good choice!".format(chosen))
    else:
        print("That is not an available option.")
        print(menu)

else:
    print("Goodbye!")
