import requests

# parameters for creating a user in pixela

user_params ={
    "token":"ahienfeofiefned",
    "username":"prayag",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",

}

#creating a user in pixela, once this is run succesfully user is created
response = requests.post(url="https://pixe.la/v1/users", json=user_params)
print(response.text)