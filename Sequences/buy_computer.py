available_parts = [("computer", 100),
                   ("monitor", 20),
                   ("keyboard", 5),
                   ("mouse", 5),
                   ("hdmi cable", 2),
                   ("dvd drive", 10)
                   ]

# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))

current_choice = "-"
computer_parts = [] # create an empty list

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        part = available_parts[index][0]
        if chosen_part in computer_parts:
            # it's already in, so remove it
            print("Removing {}".format(part))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(part))
            computer_parts.append(chosen_part)

        total_price = 0
        print("Your list now contains:")
        for (part, price) in computer_parts:
            print(part)
            total_price = total_price + price
        print(total_price)

    else:
        print("please add options from the list below (choose '0' to exit)")
        for number, (part, price) in enumerate(available_parts):
            print("{0}: {1} \t £{2}".format(number + 1, part, price))

    current_choice = input()

print(computer_parts)
