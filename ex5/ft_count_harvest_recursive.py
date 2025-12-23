def ft_count_harvest_recursive(i, total):
    print("Days until harvest:")
    days = int(input())
    if i > total:
        return
    print("Day", i)
    ft_count_harvest_recursive(i + 1, total)
    print("Harvest time!")