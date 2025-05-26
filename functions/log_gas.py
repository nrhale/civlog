from functions.utils import (
    get_data,
    input_date,
    input_mileage,
    input_number,
    update_data,
)


def log_gas():
    print("# LOG GAS")

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

    data = get_data()
    data["gas"].append(log)
    update_data(data)

    print("GAS LOGGED\n")
