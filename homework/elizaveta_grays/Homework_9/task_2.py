temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]


def hot_days(x):
    if x > 28:
        return True
    return False


new_temperatures = list(filter(hot_days, temperatures))

print(max(new_temperatures))
print(min(new_temperatures))
print(sum(new_temperatures) / len(new_temperatures))
