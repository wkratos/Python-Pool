def ft_seed_inventory(name, quantity, seed_type):
    try:
        quantity = int(quantity)
    except (TypeError, ValueError):
        raise ValueError("quantity must be an integer")

    print(f"{name} seeds: {quantity} {seed_type}")
    return name, quantity, seed_type

sd = ft_seed_inventory("Sunflower", 50, "Flowers")