def ft_plant_age():
    age = int(input("Enter plant age in days: "))
    if age <= 60:
        print("Plant needs more time to grow.", age)
    else:
        print("Plant age is ready for harvest!", age)