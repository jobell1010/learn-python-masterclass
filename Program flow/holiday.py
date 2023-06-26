name = input("What is your name? ")
age = int(input("What age are you? "))

if 18 <= age <=30:
    print("Welcome to your holiday {}! I hope you have a great time!" .format(name))
else:
    print("I'm sorry {}, but you appear to be at the wrong place." .format(name))
