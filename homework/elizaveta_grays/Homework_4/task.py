my_dict = {
    'tuple': (2, 4, 6, 8, 10, 12),
    'list': ['eggs', 'milk', 'chees', 'apple', 'meet'],
    'dict': {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5'},
    'set': {1, 3, 5, 7, 9, 11}
}
print(my_dict['tuple'][-1])

my_dict['list'].append('tea')
my_dict['list'].pop(1)


my_dict['dict'][('i am a tuple',)] = '6'
my_dict['dict'].pop('two')

my_dict['set'].add(13)
my_dict['set'].pop()

print(my_dict)