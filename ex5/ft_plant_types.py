class Plant:
    """Base class for different types of plants."""
    def __init__(self, name, height, age_days):
        self.name = name
        self.age_days = age_days
        self.height = height

    def get_info(self):
        """Print a summary string for the plant."""
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


class Flower(Plant):
    """Represent a flower plant."""
    def __init__(self, name, height, age_days, color):
        super().__init__(name, height, age_days)
        self.color = color

    """Make the flower bloom."""
    def bloom(self):
        return (
            f"{self.name} is blooming with {self.color} petals."
        )


class Tree(Plant):
    """Represent a tree plant."""
    def __init__(self, name, height, age_days, trunk_diameter):
        super().__init__(name, height, age_days)
        self.trunk_diameter = trunk_diameter

    """Produce shade based on trunk diameter."""
    def produce_shade(self):
        return (
            f"{self.name} produces shade with a trunk diameter of "
            f"{self.trunk_diameter}."
        )


class Vegetable(Plant):
    """Represent a vegetable plant."""
    def __init__(self, name, height, age_days, harvest_season,
                 nutritional_value):
        super().__init__(name, height, age_days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
