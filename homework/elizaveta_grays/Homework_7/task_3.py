my_list = ['результат операции: 42', 'результат операции: 54', 'результат работы программы: 209', 'результат: 2']


def process_result(result_string):
    sym = result_string.index(':')
    text = result_string[sym + 1:]
    text = text.strip()
    res = int(text) + 10
    print(res)


for item in my_list:
    process_result(item)
