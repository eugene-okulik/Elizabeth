for a in range(1, 101):
    if a % 3 == 0 and a % 5 == 0:
        print('FuzzBuzz')
    elif a % 3 == 0:
        print('Fuzz')
    elif a % 5 == 0:
        print('Buzz')
    else:
        print(a)
