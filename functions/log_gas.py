import json
import os
from .utils.input_date import input_date
from .utils.input_number import input_number


def log_gas():
    print("LOG GAS")

    date = input_date()
    litres = input_number("LITRES: ")
    dollarsPerLitre = input_number("DOLLARS PER LITRE: ")
    total = input_number("TOTAL: ")

    gas_log = {
        "date": date,
        "litres": litres,
        "dollarsPerLitre": dollarsPerLitre,
        "total": total,
    }

    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "..", "civData.json")
    with open(file_path, "r") as file:
        data = json.load(file)
    data["gas"].append(gas_log)
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)

    print("GAS LOGGED")
