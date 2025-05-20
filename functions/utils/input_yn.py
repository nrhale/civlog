def input_yn(prompt):
    while True:
        response = input(prompt + " (Y/N): ").strip().lower()
        if response in ("y", "n"):
            return response
        print("INVALID INPUT. ENTER Y/N.")
