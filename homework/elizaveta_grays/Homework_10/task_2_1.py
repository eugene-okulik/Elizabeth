def repeat_me2(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat_me2(count=2)
def example(text):
    print(text)


example('print me')
