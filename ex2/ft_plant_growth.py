class Plant:
    def __init__(self, name, height, age_days):
        self.name = name
        self.age_days = age_days
        self.height = height

    def grow(self):
        self.height += 1

    def age(self):
        self.age_days += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


if __name__ == "__main__":
    print("=== Day 1 ===")
    rose = Plant("Rose", 25, 30)
    before = rose.height
    rose.get_info()
    print("=== Day 7 ===")

    for i in range(6):
        rose.grow()
        rose.age()

    after = rose.height
    rose.get_info()
    print(f"Growth this week: +{after - before}cm")
