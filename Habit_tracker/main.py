import requests
from datetime import datetime


USERNAME = 'ephraim'
PASSWORD = 'laioheldnceqpuhcn'
MY_GRAPH = 'graph1'


pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': PASSWORD,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id': MY_GRAPH,
    'name': 'Piano Practice',
    'unit': 'minute',
    'type': 'int',
    'color': 'momiji'
}

headers = {
    'X-USER-TOKEN': PASSWORD
}

pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{MY_GRAPH}'

today = datetime(year=2023, month=7, day=6)
print(today.strftime('%Y%m%d'))

pixel_params = {
    'date': today.strftime("%Y%m%d"),
    'quantity': '120'
}

put_params = {
    'quantity': '110'
}
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{MY_GRAPH}/{today.strftime('%Y%m%d')}"


response = requests.delete(url=update_pixel_endpoint, headers=headers)
print(response.text)