
import requests
from datetime import datetime

TOKEN = "gshd445kajsu666777sbsbs"
USERNAME = "betimoni123"
GRAPH_ID = "graphmy"

today = datetime(year=2023, month=10, day=22)

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token" : TOKEN ,
    "username" :USERNAME ,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Study",
    "unit" : "Km",
    "type" : "float",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

post_body = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "5.5",

}


# response = requests.post(url=pixel_endpoint, json=post_body, headers=headers)
# print(response.text)

update_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel = {
    "quantity": "30"
}
# response = requests.put(url=update_endpoint, json=new_pixel, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)