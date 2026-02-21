# DESCRIPTION : Adding Pages_you_may_like feature 

import json

def load_data(filename):
    with open(filename , "r") as f:
        data = json.load(f)
    return data

# Function to find pages user might like based on common interests: 
def pages_you_might_like(user_id , data):
    # Dictionary to store user interaction : 
    user_pages = {}
    for user in data['users']:
        user_pages[user['id']] = set(user['liked_pages'])
    
    # If the user is not found : 
    if user_id not in user_pages : 
        return []
    
    user_liked_pages = user_pages[user_id]

    page_suggestions = {}

    for other_user , pages in user_pages.items():
        if other_user != user_id:
            shared_pages = user_liked_pages.intersection(pages)
        for page in pages : 
            if page not in user_liked_pages : 
                page_suggestions[page] = page_suggestions.get(page , 0) + len(shared_pages)
    
    sorted_pages = sorted(page_suggestions.items() , key = lambda x : x[1] , reverse = True)
    return [(page_id , score) for page_id , score in sorted_pages]


data = load_data("raw_data.json")
user_id = int(input("Can you please give the user id ? :"))
recommendations = pages_you_might_like(user_id, data)
print(f"People You May like pages {user_id}: {recommendations}")