import datetime
from pathlib import Path

file_path = Path.home() / 'PycharmProjects/Elizabeth/homework/eugene_okulik/hw_13/data.txt'


def read_file():
    with open(file_path, 'r') as data_file:
        for line in data_file.readlines():
            yield line


def process_line(line):
    parts = line.split(' - ')
    date_str = parts[0].split('. ')[1]
    data_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
    text = parts[1]
    if not line.strip():
        return
    if 'на неделю позже' in text:
        new_date = data_obj + datetime.timedelta(days=7)
        print(new_date)
    elif 'день недели' in text:
        week = data_obj.strftime('%A')
        print(week)
    elif 'дней назад' in text:
        now = datetime.datetime.now()
        date_ago = now - data_obj
        print(date_ago.days)


for line in read_file():
    process_line(line)
