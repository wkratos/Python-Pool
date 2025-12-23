def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def print_day(i, total):
        if i > total:
            return
        print("Day", i)
        print_day(i + 1, total)

    print_day(1, days)
    print("Harvest time!")