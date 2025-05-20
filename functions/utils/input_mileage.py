from .input_yn import input_yn
from .input_number import input_number


def input_mileage():
    if input_yn("mileage") == "y":
        return input_number("mileage: ")
    return "n"
