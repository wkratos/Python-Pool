def validate_ingredients(ingredients: str) -> str:
    allowed = {"fire", "water", "earth", "air"}
    words = ingredients.split()
    for word in words:
        if word not in allowed:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
