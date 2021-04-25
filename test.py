import requests

login = input('your login: ')
password = input('your password: ')

response = requests.post('http://127.0.0.1:5000/register/', json={'login': login, 'password': password})

print(response.text)
print(response.status_code)

count = 0

while count < 3:

    login2 = input('your login: ')
    password2 = input('your password: ')

    count += 1

    response = requests.post('http://127.0.0.1:5000/login/', json={'login': login2, 'password': password2})
    print(response.text)
    print(response.status_code)

else:
    print('You\'ve run out of attempts!')
