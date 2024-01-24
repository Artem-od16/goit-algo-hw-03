from datetime import datetime

def get_days_from_today(date = None):
    current_datetime = datetime.today()

    while True:
        if date is None:
            date = input("Write a date in format YYYY.MM.DD (for instance - 2012.12.20): ")

        try:
            datetime_object = datetime.strptime(date, "%Y.%m.%d")
            current_date = current_datetime.date()
            target_date = datetime_object.date()
            difference = current_date - target_date

            if -1 <= difference.days <= 1:
                print(
                    """Result : 
                    There is no significant difference; 
                    you either wrote today's date or 
                    the date is within one day of today."""
                )
            else:
                print(f"Result : The difference is {difference.days} days.")
            break
        except ValueError as error:
            print("1. You wrote date in wrong format")
            print(f"2. Error: {error}")
            print("3. Please enter a valid date")
        except Exception as error:
            print(f"Unexpected error: {error}")
        finally:
            print("- Loop is over")

get_days_from_today()  # this will prompt the user for input
get_days_from_today("2023.12.14")  # pass a date string as an argument

# example with usage of regexp

# import re
# from datetime import datetime

# current_datetime = datetime.today()
# pattern = "^\d{4}\.(?:0[1-9]|1[0-2])\.(?:0[1-9]|[12][0-9]|3[01])$"


# def get_days_from_today(date):
#     check = re.search(pattern, date)

#     if check:
#         datetime_object = datetime.strptime(date, "%Y.%m.%d")

#         current_date = current_datetime.date()
#         target_date = datetime_object.date()

#         difference = current_date - target_date

#         if difference.days > 1 or difference.days < -1:
#             print(f"The difference is {difference.days} days")
#         elif difference.days != 0:
#             print(f"The difference is {difference.days} day")
#         else:
#             print("There is no difference, you wrote today date")

#     else:
#         print("You wrote date in wrong format")


# date = input("Write a date in format YYYY.MM.DD (for instance - 2012.12.20) : ")
# get_days_from_today(date)
