import pytz
import datetime

zones = ("America/Aruba", "Europe/Warsaw", "Asia/Macau", "Indian/Cocos")
choice = 99

while choice != 0:
    if 1 <= choice <= 4:
        country = zones[choice - 1]
        tz_in_country = pytz.timezone(country)
        time_in_country = datetime.datetime.now(tz=tz_in_country)
        local_time = datetime.datetime.now()
        utc_time = datetime.datetime.utcnow()

        print(f"You have chosen {choice} which is {country}")
        print(f"The time there is {time_in_country.strftime('%a %x %X %z')}")
        print(f"The time here is {local_time.strftime('%a %x %X')}")
        print(f"UTC is {utc_time.strftime('%a %x %X')}")

    else:
        print("Please choose a timezone to display from the following list")
        for i, zone in enumerate(zones):
            print(i + 1, ": " + zone)
        print("0 : Exit program")

    choice = int(input(">"))
