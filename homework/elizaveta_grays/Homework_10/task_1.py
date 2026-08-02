def print_text(some_func):
    def wrapper(*args):
        some_func(*args)
        print('finished')

    return wrapper


@print_text
def example(text):
    print(text)


example('print me')
