import datetime

data = "Jan 15, 2023 - 12:05:33"

py_data = datetime.datetime.strptime(data, '%b %d, %Y - %H:%M:%S')
hu_date = py_data.strftime('%d.%m.%Y - %H:%M')

print(py_data.strftime('%B'))
print(hu_date)
