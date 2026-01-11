class Plant:
    def __init__(self, name, age_days, height):
        self.name = name
        self.age_days = age_days
        self.height = height

    def plant_info(self):
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 30, 25)
    tulip = Plant("Tulip", 20, 15)
    daisy = Plant("Daisy", 10, 5)

    rose.plant_info()
    tulip.plant_info()
    daisy.plant_info()
