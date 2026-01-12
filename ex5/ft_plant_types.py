class Plant:
    def __init__(self, name, height, age_days):
        self.name = name
        self.age_days = age_days
        self.height = height


class Flower(Plant):
    def __init__(self, name, height, age_days, color):
        super().__init__(name, height, age_days)
        self.color = color

    def bloom(self):
        return (
            f"{self.name} is blooming with {self.color} petals."
        )


class Tree(Plant):
    def __init__(self, name, height, age_days, trunk_diameter):
        super().__init__(name, height, age_days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        return (
            f"{self.name} produces shade with a trunk diameter of "
            f"{self.trunk_diameter}."
        )


class Vegetable(Plant):
    def __init__(
        self,
        name,
        height,
        age_days,
        harvest_season,
        nutritional_value,
    ):
        super().__init__(name, height, age_days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
