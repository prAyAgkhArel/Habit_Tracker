import requests
username = "prayag"
token="ahienfeofiefned"
# parameters for creating a user in pixela

# user_params ={
#     "token":"ahienfeofiefned",
#     "username":"prayag",
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes",
#
# }

#creating a user in pixela, once this is run succesfully user is created
# response = requests.post(url="https://pixe.la/v1/users", json=user_params)
# print(response.text)

#creating a graph, parameters are known from pixela api docs

graph_parameters = {
    "id":"graph1",
    "name":"Cycling Graph",
    "unit":"km",
    "type":"float",
    "color":"sora"
}

# token is given as headers as it should be confidential so it is not given directly in url as parameter
# but as a headers "X-USER-TOKEN" as suggested by API docs.

headers ={
    "X-USER-TOKEN":token
}

reponse = requests.post(url=f"https://pixe.la/v1/users/{username}/graphs",json=graph_parameters,headers=headers)