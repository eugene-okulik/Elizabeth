my_list = ['результат операции: 42', 'результат операции: 514', 'результат работы программы: 9']

sym = my_list[0].index(':')
text = my_list[0][sym + 1:]
text = text.strip()
res = int(text) + 10
print(res)

sym = my_list[1].index(':')
text = my_list[1][sym + 1:]
text = text.strip()
res = int(text) + 10
print(res)

sym = my_list[2].index(':')
text = my_list[2][sym + 1:]
text = text.strip()
res = int(text) + 10
print(res)
