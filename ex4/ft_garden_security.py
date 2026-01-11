class SecurePlant:
    def __init__(self, name, height, age_days):
        self.name = name
        self._height = 0
        self._age_days = 0

        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age_days)

    def set_height(self, new_height):
        if new_height < 0:
            print("\n")
            print(f"Invalid operation attempted: height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
            print("\n")
            return
        self._height = new_height
        print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, new_age):
        if new_age < 0:
            print("\n")
            print(f"Invalid operation attempted: age {new_age} days [REJECTED]")
            print("Security: Negative age rejected")
            print("\n")
            return
        self._age_days = new_age
        print(f"Age updated: {self._age_days} days [OK]")

    def display_info(self):
        print(f"Current plant: {self.name} ({self._height}cm, {self._age_days} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose", 25, 30)
    plant.set_height(-5)
    plant.display_info()
