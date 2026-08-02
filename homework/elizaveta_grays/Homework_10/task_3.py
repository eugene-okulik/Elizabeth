def choose_operation(calc):
    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = '*'
            return calc(first, second, operation)
        elif first == second:
            operation = '+'
            return calc(first, second, operation)
        elif first > second:
            operation = '-'
            return calc(first, second, operation)
        elif second > first:
            operation = '/'
            return calc(first, second, operation)

    return wrapper


@choose_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

print(calc(num1, num2))
