class Plant:
    """Represent a plant instance and track total created."""

    plant_count = 0

    def __init__(self, name, height, age_days):
        """Initialize a plant and increment the factory count."""
        self.name = name
        self.age_days = age_days
        self.height = height
        Plant.plant_count += 1

    def get_info(self):
        """Return a summary string for the plant."""
        return (f"Created: {self.name} ({self.height}cm, "
                f"{self.age_days} days)")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)
    plants = [rose, oak, cactus, sunflower, fern]
    for plant in plants:
        plant.get_info()
    print(f"\nTotal plants created: {Plant.plant_count}")
