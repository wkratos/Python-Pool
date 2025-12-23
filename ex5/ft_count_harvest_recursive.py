print("Days until harvest:")
days = int(input())

def print_days(i, total):
    if i > total:
        return
    print("Day", i)
    print_days(i + 1, total)

print_days(1, days)
print("Harvest time!")