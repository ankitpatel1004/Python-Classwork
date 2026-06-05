try:
    age = 9
    if age < 18:
        raise ValueError("Age must be 18 for registration")
except ValueError as e:
    print("Error:", e)

