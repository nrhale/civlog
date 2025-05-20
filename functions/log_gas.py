import json
import os
from dotenv import load_dotenv
from .utils.input_date import input_date
from .utils.input_number import input_number
from .utils.input_mileage import input_mileage


def log_gas():
    print("LOG GAS")

    date = input_date()
    litres = input_number("LITRES: ")
    dollarsPerLitre = input_number("DOLLARS PER LITRE: ")
    total = input_number("TOTAL: ")
    mileage = input_mileage()

    log = {
        "date": date,
        "litres": litres,
        "dollarsPerLitre": dollarsPerLitre,
        "total": total,
    }
    if mileage != "n":
        log["mileage"] = mileage

    load_dotenv()
    file_path = os.getenv("CIVLOG_DATA_PATH")
    with open(file_path, "r") as file:
        data = json.load(file)
    data["gas"].append(log)
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)

    print("GAS LOGGED")
