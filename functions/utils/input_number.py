def input_number(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("INVALID INPUT. ENTER A NUMBER.")
