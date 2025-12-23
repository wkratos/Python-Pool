def ft_plant_age():
    print("Enter plant age in days:")
    age = int(input())
    if age <= 60:
        print("Plant needs more time to grow.", age)
    else:
        print("Plant age is ready for harvest!", age)