import requests


response = requests.get('http://192.168.31.26:5000/app/api/details/all')
print(response.status_code)
print(response.json())


# response = requests.get('http://127.0.0.1:5000/app/api/details/all')
# print(response.status_code)
# print(response.json())

# response = requests.get('http://127.0.0.1:5000/app/api/courses?id=1')
# print(response.status_code)
# print(response.json())


