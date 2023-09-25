available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }

parts_list = []
current_choice = None
while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if chosen_part in parts_list:
            print(f"Removing {chosen_part}")
            parts_list.remove(chosen_part)
        else:
            print(f"Adding {chosen_part}")
            parts_list.append(chosen_part)

        print("Your parts list currently contains:")
        print(parts_list)
    else:
        print("Please add options from the list")
        for key, part in available_parts.items():
            print(f"{key}: {part}")
        print("0: to finish")

    current_choice = input("> ")
