from datetime import datetime


def input_date():
    while True:
        user_input = input("DATE (YYYY-MM-DD): ")
        try:
            return str(datetime.strptime(user_input, "%Y-%m-%d").date())
        except ValueError:
            print("INVALID FORMAT. USE YYYY-MM-DD.")
