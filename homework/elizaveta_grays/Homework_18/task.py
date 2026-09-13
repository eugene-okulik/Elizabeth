import requests


def all_object():
    response = requests.get('http://objapi.course.qa-practice.com/object').json()
    print(response)


def one_object():
    response = requests.get('http://objapi.course.qa-practice.com/object/1').json()
    print(response)


def post_object():
    body = {
        'name': 'Test123',
        'data': {'color': 'pink', 'size': 's'}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers).json()
    print(response)


def put_object():
    body = {
        'name': 'Test',
        'data': {'color': 'blue', 'size': 'm'}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put('http://objapi.course.qa-practice.com/object/14', json=body, headers=headers).json()
    print(response)


def patch_object():
    body = {
        'name': 'Test1'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch('http://objapi.course.qa-practice.com/object/14', json=body, headers=headers).json()
    print(response)


def delete_object():
    response = requests.delete('http://objapi.course.qa-practice.com/object/14')
    print(response.status_code)


all_object()
one_object()
post_object()
put_object()
patch_object()
delete_object()
