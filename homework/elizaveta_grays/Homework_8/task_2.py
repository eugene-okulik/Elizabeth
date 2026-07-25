import sys

sys.set_int_max_str_digits(30000)


def generation():
    n1 = 0
    n2 = 1
    while True:
        yield n1
        n1, n2 = n2, n1 + n2


def print_number(k):
    count = 0
    for number in generation():
        count += 1
        if count == k:
            print(number)
            break


print_number(5)
print_number(200)
print_number(1000)
print_number(100000)
