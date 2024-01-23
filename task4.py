from datetime import datetime, timedelta

current_datetime = datetime.now()
current_year = current_datetime.year


def get_upcoming_birthdays(users: list):
    new_users_list = []

    for person in users:
        date = person["birthday"]
        datetime_object = datetime.strptime(date, "%Y.%m.%d")
        day = datetime_object.weekday()

        if day == 6:
            day_interval = timedelta(days=2)
            datetime_object = datetime_object + day_interval
        elif day == 7:
            day_interval = timedelta(days=1)
            datetime_object = datetime_object + day_interval

        target_day = datetime_object.day

        date = str(current_year) + date[4:8] + str(target_day)

        del person["birthday"]
        person["congratulation_date"] = date
        new_users_list.append(person)

    return new_users_list


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.26"},
]

upcoming_birthdays = get_upcoming_birthdays(users)

print("This week's list of greetings:")
for person_birthday in upcoming_birthdays:
    print(person_birthday)
