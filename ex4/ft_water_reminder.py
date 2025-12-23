def ft_water_reminder():
    print("Days since last watering:")
    days = int(input())
    if days >= 2:
        print("Water the plants!")
    else:
        print("Plants are fine")