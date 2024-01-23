import re
from datetime import datetime

current_datetime = datetime.today()
pattern = "^\d{4}\.(?:0[1-9]|1[0-2])\.(?:0[1-9]|[12][0-9]|3[01])$"


def get_days_from_today(date):
    check = re.search(pattern, date)

    if check:
        datetime_object = datetime.strptime(date, "%Y.%m.%d")

        current_date = current_datetime.date()
        target_date = datetime_object.date()

        difference = current_date - target_date

        if difference.days > 1 or difference.days < -1:
            print(f"The difference is {difference.days} days")
        elif difference.days != 0:
            print(f"The difference is {difference.days} day")
        else:
            print("There is no difference, you wrote today date")

    else:
        print("You wrote date in wrong format")


date = input("Write a date in format YYYY.MM.DD (for instance - 2012.12.20) : ")
get_days_from_today(date)
