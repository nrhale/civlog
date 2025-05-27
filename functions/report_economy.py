from functions.utils import get_data, input_selection


def report_economy():
    print("# REPORT FUEL ECONOMY")
    print("1. TOTAL AVERAGE")
    print("2. LATEST AVERAGE")
    print("3. GO BACK")
    selection = input_selection(3)

    if selection == 1:
        data = get_data()
        initial_mileage = data["initialPurchase"]["mileage"]

        for log in reversed(data["gas"]):
            if "mileage" in log:
                final_mileage = log["mileage"]

        total_litres = 0
        for log in data["gas"]:
            total_litres += log["litres"]

        print(
            "TOTAL AVERAGE FUEL ECONOMY: ",
            round(total_litres / (final_mileage - initial_mileage) * 100, 2),
            "\n",
        )

    elif selection == 2:
        pass
