from datetime import datetime
import json
import os
from dotenv import load_dotenv


def input_number(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("INVALID INPUT. ENTER A NUMBER.")


def input_date():
    while True:
        user_input = input("DATE (YYYY-MM-DD): ")
        try:
            return str(datetime.strptime(user_input, "%Y-%m-%d").date())
        except ValueError:
            print("INVALID FORMAT. USE YYYY-MM-DD.")


def input_yn(prompt):
    while True:
        response = input(prompt + " (Y/N): ").strip().lower()
        if response in ("y", "n"):
            return response
        print("INVALID INPUT. ENTER Y/N.")


def input_mileage():
    if input_yn("mileage") == "y":
        return input_number("mileage: ")
    return "n"


def input_selection(count):
    while True:
        user_input = input("SELECTION: ")
        if user_input.isdigit():
            selection = int(user_input)
            if 0 < selection < count + 1:
                print()
                return selection
        print("INVALID SELECTION.")


def get_data():
    load_dotenv()
    with open(os.getenv("CIVLOG_DATA_PATH"), "r") as file:
        return json.load(file)


def update_data(data):
    with open(os.getenv("CIVLOG_DATA_PATH"), "w") as file:
        json.dump(data, file, indent=2)
