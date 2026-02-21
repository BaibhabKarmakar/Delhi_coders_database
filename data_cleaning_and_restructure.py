# DESCRIPTION : Cleaning the Data and restructuring the data : 
# "data2.json" file have some serious mistakes in the json data . It have some blank or null entries , have some duplicate entries , duplicate ids . We need to clean and restructure the data as we are going to be data scientists . 

# load the data : 
import json

def load_data(filename):
    with open(filename , "r") as f:
        data = json.load(f)
    return data

# print(data , type(data))

def clean_data(data):
    # remove users with missing names : 
    data['users'] = [user for user in data['users'] if user['name'].strip()]

    # Remove duplicate friends : 
    for user in data['users']:
        user['friends'] = list(set(user['friends']))

    # remove the inactive records : 
    data['users'] = [user for user in data['users'] if user['liked_pages'] or user['friends']]

    # remove duplicate pages : 
    unique_pages = {}
    for page in data['pages']:
        unique_pages[page['id']] = page
    data['pages'] = list(unique_pages.values())
    return data



# load the data : 
data = load_data("raw_data.json")
cleaned_data = clean_data(data)
json.dump(cleaned_data , open("cleaned_data.json" , "w") , indent = 2)
print("Data has been cleaned and saved!")



