# DESCRIPTION : Firstly load the data from the json file and then analyse it for good insights . 

import json

# Lets write a function to load the data : 
def load_data(filename):
    with open(filename , "r") as f:
        data = json.load(f)
    return data

data = load_data("data.json")
# print(data , type(data))

# Now writing a code which will display the users and their connections . 
def display_users(data):
    print("USERS AND THEIR CONNECTIONS : \n")
    for user in data['users']:
        print(f" {user['id']} : {user['name']} and friends with : {user['friends']} and liked pages are : {user['liked_pages']} ")
    print("\nPages information : \n")
    for page in data['pages']:
        print(f" {page['id']} : {page['name']} ")

display_users(data)
