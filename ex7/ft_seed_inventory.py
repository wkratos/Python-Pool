def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    s = seed_type
    seed = s.capitalize()
    if unit == "packets":
        print(seed, "seeds:", quantity, "packets available")
    elif unit == "grams":
        print(seed, "seeds:", quantity, "grams total")
    elif unit == "area":
        print(seed, "seeds:", "covers", quantity, "square meters")
    else:
        print("Unknown type")
