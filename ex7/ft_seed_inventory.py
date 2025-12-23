def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    try:
        quantity = int(quantity)
    except (TypeError, ValueError):
        raise ValueError("quantity must be an integer")

    print(f"{seed_type} seeds: {quantity} {unit}")